from django.shortcuts import render
from django.template.loader import render_to_string
from .forms import *
from .models import *


def part_edit(request):
    form = PartForm()
    if request.method == 'POST':
        form = PartForm(request.POST)
        if form.is_valid():
            form.save()
            form = PartForm()
    parts = Part.objects.all().order_by('type__sort', 'broken')
    # context = {'form': form}
    context = {'parts': parts, 'form': form}
    return render(request, 'inventory/part_edit.html', context)
