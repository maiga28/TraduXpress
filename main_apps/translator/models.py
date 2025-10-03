from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    translated_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.file)
