from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from corecode.models import StudentClass

from students.models import Student

from .forms import InvoiceItemFormset, InvoiceReceiptFormSet, Invoices
from .models import Invoice, InvoiceItem, Receipt

# Staff Part of the code


def invoicelist(request, pk):
    cl= StudentClass.objects.get(id=pk)
    invoices = Invoice.objects.filter(class_for=cl)
    count = len(invoices)
    context ={
        'invoices': invoices,
        'count': count
    }
    return render(request, "finance/invoice-list.html", context)


class InvoiceListView(LoginRequiredMixin, ListView):
    model = Invoice


class InvoiceCreateView(LoginRequiredMixin, CreateView):
    model = Invoice
    fields = "__all__" 
    success_url = "/finance/list"

    def get_context_data(self, **kwargs):
        context = super(InvoiceCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["items"] = InvoiceItemFormset(
                self.request.POST, prefix="invoiceitem_set"
            )
        else:
            context["items"] = InvoiceItemFormset(prefix="invoiceitem_set")   
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context["items"] 
        self.object = form.save()
        if self.object.id != None:
            if form.is_valid() and formset.is_valid():
                formset.instance = self.object
                formset.save()
        return super().form_valid(form)


class InvoiceDetailView(LoginRequiredMixin, DetailView):
    model = Invoice
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super(InvoiceDetailView, self).get_context_data(**kwargs)
        context["receipts"] = Receipt.objects.filter(invoice=self.object)
        context["items"] = InvoiceItem.objects.filter(invoice=self.object)
        return context


class InvoiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Invoice
    fields = ["student", "session", "term", "class_for", "balance_from_previous_term"]

    def get_context_data(self, **kwargs):
        context = super(InvoiceUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["receipts"] = InvoiceReceiptFormSet(
                self.request.POST, instance=self.object
            )
            context["items"] = InvoiceItemFormset(
                self.request.POST, instance=self.object
            )
        else:
            context["receipts"] = InvoiceReceiptFormSet(instance=self.object)
            context["items"] = InvoiceItemFormset(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context["receipts"]
        itemsformset = context["items"]
        if form.is_valid() and formset.is_valid() and itemsformset.is_valid():
            form.save()
            formset.save() 
            itemsformset.save()
        return super().form_valid(form)


class InvoiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Invoice
    success_url = reverse_lazy("invoice-list")


class ReceiptCreateView(LoginRequiredMixin, CreateView):
    model = Receipt
    fields = ["amount_paid", "date_paid", "comment"]
    success_url = reverse_lazy("invoice-list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        invoice = Invoice.objects.get(pk=self.request.GET["invoice"])
        obj.invoice = invoice
        obj.save()
        return redirect("invoice-list")

    def get_context_data(self, **kwargs):
        context = super(ReceiptCreateView, self).get_context_data(**kwargs)
        invoice = Invoice.objects.get(pk=self.request.GET.get("invoice"))
        context["invoice"] = invoice
        return context


class ReceiptUpdateView(LoginRequiredMixin, UpdateView):
    model = Receipt
    fields = ["amount_paid", "date_paid", "comment"]
    success_url = reverse_lazy("invoice-list")


class ReceiptDeleteView(LoginRequiredMixin, DeleteView):
    model = Receipt
    success_url = reverse_lazy("invoice-list")

 
# Student Part of the Code

def paymentdetail(request, pk):
    student = Student.objects.get(id=pk)
    stu = student.id
    invoice = get_object_or_404(Invoice, student=stu)
    receipts = Receipt.objects.filter(invoice=invoice)
    items = InvoiceItem.objects.filter(invoice=invoice)
    context = {
        "invoices": invoice,
        "student": student,
        "receipts":receipts,
        "items": items,
    }
    return render(request, "finance/payment.html", context)


# def create_receipt(request, pk):
#     invoice = Invoice.objects.get(id=pk)
#     form = InvoiceReceiptFormSet(queryset=Receipt.objects.none(), instance=invoice)
#     if request.method == "POST":
#         form = InvoiceReceiptFormSet(request.POST, instance=invoice)
#         if form.is_valid():
#             form.save()
#             return redirect("invoice-detail", invoice.id)
#     else:
#         form = InvoiceReceiptFormSet(instance=invoice)
#     return render(request, "finance/receipt_form.html", {"form":form, "invoice":invoice})

