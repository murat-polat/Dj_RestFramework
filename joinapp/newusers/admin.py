from django.contrib import admin
from .models import NewUser


class NewUserAdmin(admin.ModelAdmin):
    list_display= ('name','username','email')


admin.site.register(NewUser,NewUserAdmin)


