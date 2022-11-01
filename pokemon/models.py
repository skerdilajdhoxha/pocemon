from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=256)
    moves = models.CharField(max_length=256)
    ability = models.CharField(max_length=256)
    experience = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Pokemon"
