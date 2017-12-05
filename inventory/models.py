import time
from django.db import models
from monitoring.models import Worker


class PartType(models.Model):
    type = models.CharField(max_length=255)
    sort = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.type


class Part(models.Model):
    type = models.ForeignKey(PartType)
    part = models.CharField(max_length=255)
    serial = models.CharField(max_length=255, unique=True)
    broken = models.BooleanField(default=False)
    last_update = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ('part', 'serial')
        verbose_name = 'Деталь'
        verbose_name_plural = 'Детали'

    def __str__(self):
        return self.part + ' ' + self.serial


class WorkerPart(models.Model):
    worker = models.ForeignKey(Worker)
    part = models.ManyToManyField(Part, null=True, default=None, blank=True)
    last_update = models.DateTimeField(auto_now=True)

    def get_parts(self):
        return "\n".join([str(p.type)+': '+ str(p.part) for p in self.part.all()])

    class Meta:
        verbose_name = 'Детали в ригах'
        verbose_name_plural = 'Детали в ригах'
