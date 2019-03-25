from django.contrib import admin
from . models import Tutorial
from tinymce.widgets import TinyMCE
from django.db import models


#  this is a way you can change the order of how your models shows on the Admin
class TutorialAdmin(admin.ModelAdmin):
    # fields = ["tutorial_title", "tutorial_content", "tutorial_published"]
    fieldsets = [
        ('Title/date', {"fields": ["tutorial_title", "tutorial_published"]}),
        ("Content", {"fields": ["tutorial_content"]})
    ]
    formfield_overide = { 
        models.TextField: {'widgets': TinyMCE()}
    }

admin.site.register(Tutorial, TutorialAdmin)