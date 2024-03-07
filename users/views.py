from django.http import HttpResponse
from django.template import loader
from .models import User
from .models import CoreSubject

def users(request):
    myusers = User.objects.all().values()
    template = loader.get_template('all_users.html')
    context = {
        'myusers': myusers,
    }

    return HttpResponse(template.render(context, request))

def userDetails(request, id):
    myuser = User.objects.get(id = id)
    template = loader.get_template('user_details.html')
    context = {
        'myuser': myuser,
    }

    return HttpResponse(template.render(context, request))

def subjectDetails(request, course_name):
    subject = CoreSubject.objects.get(course_name = course_name)
    template = loader.get_template('subject_details.html')
    context = {
        'subject' : subject,
    }

    return HttpResponse(template.render(context, request))

def subjects(request):
    subject = CoreSubject.objects.all().values()
    template = loader.get_template('all_subjects.html')
    context = {
        'subject' : subject,
    }

    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())