from django.db import models

# Table to hold holiday
class Holiday(models.Model):
    holiday_id = models.AutoField(primary_key=True)
    holiday_type = models.CharField(max_length=8)
    holiday_desc = models.CharField(max_length=15)
    holiday_date = models.DateField()
    recurr = models.CharField(max_length=2)
