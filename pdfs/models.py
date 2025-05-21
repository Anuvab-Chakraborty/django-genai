from django.db import models
from django.contrib.auth.models import User

class PDFFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pdfs")
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="pdfs/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class PDFChunk(models.Model):
    pdf = models.ForeignKey(PDFFile, on_delete=models.CASCADE, related_name="chunks")
    text = models.TextField()
    chunk_index = models.IntegerField()  # To keep the order of chunks

    def __str__(self):
        return f"Chunk {self.chunk_index} of {self.pdf.title}"
