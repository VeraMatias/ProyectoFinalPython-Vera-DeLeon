from django.contrib import admin

from Usuario.models import Avatar, InfoExtra

# Register your models here.

admin.site.register(InfoExtra)
admin.site.register(Avatar)