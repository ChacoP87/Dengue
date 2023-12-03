from django.db import models

# Create your models here.

class Prediction(models.Model):
    hemorragicos = models.BooleanField()
    diabetes = models.BooleanField()
    hipertension = models.BooleanField()
    ENFERMEDAD_ULC_PEPTICA = models.BooleanField()
    ENFERMEDAD_RENAL = models.BooleanField()
    INMUNOSUPR = models.BooleanField()
    CIRROSIS_HEPATICA = models.BooleanField()
    DEFUNCION = models.BooleanField()
