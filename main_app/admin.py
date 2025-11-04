# ফাইল: main_app/admin.py

from django.contrib import admin
from .models import TeamMember, AppDownload

admin.site.register(TeamMember)
admin.site.register(AppDownload)