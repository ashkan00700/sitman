from django.db import models
from django.contrib.auth.models import User

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    is_advertisement = models.BooleanField(default=False, verbose_name="تبلیغ برای ادمین")
    is_approved = models.BooleanField(default=False, verbose_name="تأیید توسط ادمین")
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name