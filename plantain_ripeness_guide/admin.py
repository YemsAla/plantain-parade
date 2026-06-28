from django.contrib import admin
from .models import RipenessGuide


@admin.register(RipenessGuide)
class RipenessGuideAdmin(admin.ModelAdmin):
    list_display = ('stage', 'description', 'best_uses', 'cooking_tips')
