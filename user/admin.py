from django.contrib import admin

from user.models import Teacher
from user.models.student_models import Student
from user.models.user_models import User
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    ordering = ['email']
    list_display = ['id', 'email', 'first_name', 'last_name', 'is_staff', 'user_type']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('id', 'first_name', 'last_name', 'gender')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_type', 'groups', 'user_permissions',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['id', 'email']
        return []

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )
    search_fields = ('email',)


# Register your models here.
admin.site.register(User, CustomUserAdmin)
admin.site.register(Student)
admin.site.register(Teacher)