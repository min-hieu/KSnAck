from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student


class StudentAdmin(UserAdmin):
    list_display = ('student_id','username','rank','happiness','date_joined','last_login','is_admin','is_staff')
    search_fields = ('student_id','username',)
    readonly_fields = ('date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Student, StudentAdmin)