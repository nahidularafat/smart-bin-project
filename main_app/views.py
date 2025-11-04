# ফাইল: main_app/views.py

from django.shortcuts import render
from .models import TeamMember, AppDownload

def home_page(request):
    try:
        ceo = TeamMember.objects.get(role='CEO')
    except TeamMember.DoesNotExist:
        ceo = None

    try:
        cto = TeamMember.objects.get(role='CTO')
    except TeamMember.DoesNotExist:
        cto = None

    try:
        cfo = TeamMember.objects.get(role='CFO')
    except TeamMember.DoesNotExist:
        cfo = None

    try:
        # ডেটাবেস থেকে সর্বশেষ আপলোড করা অ্যাপ ফাইলটি খুঁজে বের করবে
        latest_app = AppDownload.objects.latest('uploaded_at')
    except AppDownload.DoesNotExist:
        latest_app = None

    context = {
        'ceo': ceo,
        'cto': cto,
        'cfo': cfo,
        'app_file': latest_app,
    }
    return render(request, 'index.html', context)