from django.db import models

# Create your models here.
class Contactmessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    submitted_on = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.name} - {self.subject}"

