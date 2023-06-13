from django.db import models
from apps.polling_units.models import PollingUnit


class AgentName(models.Model):
    name_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    polling_unit = models.ForeignKey(PollingUnit, on_delete=models.CASCADE)
    user_ip_address = models.CharField(max_length=50)
    date_entered = models.DateTimeField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
