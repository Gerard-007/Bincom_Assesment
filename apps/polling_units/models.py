from django.db import models


class State(models.Model):
    state_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return self.state_name


class LGA(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    lga_id = models.IntegerField()
    lga_name = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    lga_description = models.TextField(blank=True, null=True)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_created=True)
    user_ip_address = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.lga_name


class Ward(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    ward_id = models.IntegerField()
    ward_name = models.CharField(max_length=50)
    lga = models.ForeignKey(LGA, on_delete=models.CASCADE)
    ward_description = models.TextField(blank=True, null=True)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_created=True)
    user_ip_address = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.ward_name


class Party(models.Model):
    id = models.AutoField(primary_key=True)
    party_id = models.CharField(max_length=11)
    party_name = models.CharField(max_length=11)

    def __str__(self):
        return self.party_name


class PollingUnit(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    polling_unit_id = models.IntegerField()
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    lga = models.ForeignKey(LGA, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    unique_ward_id = models.IntegerField(blank=True, null=True)
    polling_unit_number = models.CharField(max_length=50, blank=True, null=True)
    polling_unit_name = models.CharField(max_length=50, blank=True, null=True)
    polling_unit_description = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=255, blank=True, null=True)
    long = models.CharField(max_length=255, blank=True, null=True)
    entered_by_user = models.CharField(max_length=50, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    user_ip_address = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Polling Unit {self.polling_unit_id} - {self.polling_unit_name}"


class PartyResult(models.Model):
    id = models.AutoField(primary_key=True)
    polling_unit = models.ForeignKey(PollingUnit, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    result = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.polling_unit
