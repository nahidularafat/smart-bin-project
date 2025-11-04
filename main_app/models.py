# ফাইল: main_app/models.py

from django.db import models

class TeamMember(models.Model):
    ROLE_CHOICES = (
        ('CEO', 'Chief Executive Officer'),
        ('CTO', 'Chief Technical Officer'),
        ('CFO', 'Chief Financial Officer'),
    )
    
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=3, choices=ROLE_CHOICES, unique=True) 
    bio = models.TextField()
    image = models.ImageField(upload_to='team_photos/')

    def __str__(self):
        return f"{self.name} - {self.get_role_display()}"

class AppDownload(models.Model):
    version_name = models.CharField(max_length=50, default="v1.0")
    apk_file = models.FileField(upload_to='apks/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SmartBin App - {self.version_name}"