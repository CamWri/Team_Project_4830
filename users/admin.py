from django.contrib import admin
from .models import User
from .models import Ticket
from .models import CoreSubject
from .models import Course

class UserAdmin(admin.ModelAdmin):
    list_display = ("firstName", "lastName", "phone", "email",)


class TicketAdmin(admin.ModelAdmin):
    list_display = ("user","title", "post_description",)

class CoreSubjectAdmin(admin.ModelAdmin):
    list_display = ("subject",)

class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_name",)


admin.site.register(User, UserAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(CoreSubject, CoreSubjectAdmin)
admin.site.register(Course, CourseAdmin)