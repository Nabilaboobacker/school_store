from django.contrib import admin
from . models import Department, Course, Material, User_profile

# Register your models here.
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Material)
admin.site.register(User_profile)