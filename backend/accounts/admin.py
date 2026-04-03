from django.contrib import admin
from .models import User, SchoolMember, Student

# Register your models here.
admin.site.register(User)
admin.site.register(SchoolMember)
admin.site.register(Student)


