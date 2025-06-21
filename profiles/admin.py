from django.contrib import admin
from .models import Organization, Staff, CustomUser
# Register your models here.

admin.site.register(Organization)
admin.site.register(Staff)
admin.site.register(CustomUser)
