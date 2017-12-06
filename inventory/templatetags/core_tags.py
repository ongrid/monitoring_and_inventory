from django import template
from django.shortcuts import get_object_or_404

from inventory.models import *

register = template.Library()


@register.filter(name='get_worker')
def get_worker(part):
    try:
        worker = WorkerPart.objects.get(part=part)
    except WorkerPart.DoesNotExist:
        return None
    return worker.worker


@register.filter(name='get_worker_parts')
def get_worker_parts(worker):
    worker_parts = get_object_or_404(WorkerPart, worker=worker)
    return worker_parts.part.get_queryset()
