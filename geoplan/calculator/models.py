from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=30)
    project_location = models.CharField(max_length=30)
    operator = models.CharField(max_length=30)
    date_started = models.DateField()


class Well(models.Model):
    well_name = models.CharField(max_length=30)
    well_location = models.CharField(max_length=30)
