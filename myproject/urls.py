# ফাইল: myproject/urls.py

from django.contrib import admin
from django.urls import path, include  # <-- 'include' যোগ করুন
from django.conf import settings      # <-- এই লাইনটি যোগ করুন
from django.conf.urls.static import static  # <-- এই লাইনটি যোগ করুন

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')), # <-- এই লাইনটি যোগ করুন
]

# মিডিয়া ফাইল দেখানোর জন্য নিচের অংশটুকু যোগ করুন
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)