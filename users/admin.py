from django.contrib import admin
from .models import User

class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstName", "lastName", "phone",)


admin.site.register(User, MemberAdmin)