from django.contrib import admin
from .models import Content, Member, Support

# Register your models here.

admin.site.register(Content)
admin.site.register(Member)
admin.site.register(Support)