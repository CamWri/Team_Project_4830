#TO DO
#Restrict Input files to respective catagories
#Create, Read, Update, Delete without admin privliges/in regular website

from django.db import models
from django.core.validators import FileExtensionValidator


class User(models.Model):
    firstName = models.CharField('First Name', max_length=50)
    lastName = models.CharField('Last Name', max_length=50)
    email = models.EmailField('Email', null=True, blank=True)
    phone = models.CharField('Phone Number', null=True, blank=True, max_length = 12)
    username = models.CharField("Username", max_length = 75)
    password = models.CharField("Password", max_length = 75)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
    
class Ticket(models.Model):
    user = models.ForeignKey(User, blank = True, null = True, on_delete = models.PROTECT)
    title = models.CharField("Title", max_length = 100)
    time_of_post = models.DateTimeField("Time of Post")
    post_description = models.CharField("Description", max_length = 500, null = True)
    pdf_file = models.FileField('PDF File', null = True, blank = True, validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc'])])
    video_file = models.FileField('Video File', null = True, blank = True)
    video_website_address = models.URLField('Video Adress', null = True, blank = True)

    def __str__(self):
        return f"{self.user} {self.title} {self.post_description}"
    
class Course(models.Model):
    course_name = models.CharField("Course", max_length = 75)
    all_tickets = models.ManyToManyField(Ticket, null = True, blank=True)
    description = models.CharField("Description", max_length = 300)

    def __str__(self):
        return f" {self.course_name}"
    
class CoreSubject(models.Model):
    subject = models.CharField("Core Subject", max_length = 75)
    courses = models.ManyToManyField(Course, null = True, blank = True)

    def __str__(self):
        return f" {self.subject}"