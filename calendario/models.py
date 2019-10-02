from django.db import models
from django.urls import reverse
from CEM.models import Doctor, Paciente

# Create your models here.
class Event(models.Model):
    idDoctor = models.ForeignKey(
        Doctor,
        on_delete = models.SET_NULL,
        null = True
    )
    expediente = models.ForeignKey(
        Paciente,
        on_delete = models.SET_NULL, 
        null = True
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    @property
    def get_html_url(self):
        url = reverse('event_detail', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'