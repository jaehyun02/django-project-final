from django.contrib import admin
from users.models import Member
# Register your models here.

@admin.register(Member)
class Member_admin(admin.ModelAdmin):
    list_display=[
        'nickname',
        'password',
        'name',
        'age',
        'createdDate',
        'updatedDate'
    ]