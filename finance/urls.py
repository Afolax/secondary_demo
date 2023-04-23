from django.urls import path

from .views import * 


urlpatterns = [
    path("history/<int:pk>/", paymentdetail, name="student-invoice"),
    path("list/<int:pk>/", invoicelist, name="invoices"),
    path("list/", InvoiceListView.as_view(), name="invoice-list"),
    path("create/", InvoiceCreateView.as_view(), name="invoice-create"),
    path("<int:pk>/detail/", InvoiceDetailView.as_view(), name="invoice-detail"),
    path("<int:pk>/update/", InvoiceUpdateView.as_view(), name="invoice-update"),
    path("<int:pk>/delete/", InvoiceDeleteView.as_view(), name="invoice-delete"),
    #path("receipt/create/", create_receipt, name="receipt-create"),
    path("receipt/create/", ReceiptCreateView.as_view(), name="receipt-create"),
    path("receipt/<int:pk>/update/", ReceiptUpdateView.as_view(), name="receipt-update"),
    
]
