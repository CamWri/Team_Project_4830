from django.http import HttpResponse
from django.template import loader
from .models import User
from .models import CoreSubject
from .models import Course

from django.shortcuts import get_object_or_404

from django.core.files.storage import FileSystemStorage

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

def subjectDetails(request, subject):
    # Retrieve the CoreSubject instance for the given subject
    core_subject = CoreSubject.objects.get(subject=subject)

    # Retrieve all courses associated with the CoreSubject
    courses = core_subject.courses.all()

    template = loader.get_template('subjects_details.html')
    context = {
        'subject': core_subject,
        'courses': courses,
    }

    return HttpResponse(template.render(context, request))


def subjects(request):
    mysubjects = CoreSubject.objects.all().values()
    template = loader.get_template('all_subjects.html')
    context = {
        'mysubjects' : mysubjects,
    }

    return HttpResponse(template.render(context, request))

def courseDetails(request, subject, course_name):
    # Retrieve the Course instance for the given subject and course name
    course = get_object_or_404(Course, course_name=course_name)

    ticket_list = course.all_tickets.all()

    template = loader.get_template('course.html')

    context = {
        'course': course,  # Pass the Course object instead of just the name
        'ticket_list': ticket_list,
    }
    
    return HttpResponse(template.render(context, request))



def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())