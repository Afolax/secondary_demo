from .models import AcademicSession, AcademicTerm, SiteConfig, StudentClass, Student_message, Staff_message


def site_defaults(request):
    current_session = AcademicSession.objects.get(current=True)
    current_term = AcademicTerm.objects.get(current=True)
    vals = SiteConfig.objects.all()
    classes = StudentClass.objects.all()
    stu_messages = Student_message.objects.all()
    stf_messages = Staff_message.objects.all()

    contexts = {
        "current_session": current_session.name,
        "current_term": current_term.name,
        "classes": classes,
        "stf_messages":stf_messages,
        "stu_messages":stu_messages,
    }
    for val in vals:
        contexts[val.key] = val.value

    return contexts
