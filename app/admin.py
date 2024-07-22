from django.contrib import admin
from .models import *

# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'phone', 'email', 'group_course')

admin.site.register(Course)
admin.site.register(Blog)
admin.site.register(Group)
admin.site.register(Feedback, FeedbackAdmin)

