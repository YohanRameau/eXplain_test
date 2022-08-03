from django.db import models


class TerritoryTypes(models.TextChoices):
    FRCOMM = 'FRCOMM'
    FREPCI = 'FREPCI'
    FRDEPA = 'FRDEPA'
    FRCANT = 'FRCANT'