from django.shortcuts import render, redirect
from django.conf import settings
from pathlib import os
from datetime import datetime
from app.models import Car

# Create your views here.
def index(request):
  list = Car.objects.all()
  return render(request, 'index.html', {'list': list})

def create(request):
  return render(request, 'form.html')

def store(request):
  if request.method == 'POST':
    car = Car()
    data = request.POST
    car.model = data.get('model')
    car.brand = data.get('brand')
    car.year = data.get('year')
    if request.FILES:
      car.filename = upload_file(request.FILES['file'])
    car.save()
    return redirect(index)

def upload_file(file):
  filename, extension = os.path.splitext(file.name)
  filename = str(datetime.now()) + extension
  with open(
    os.path.join(settings.BASE_DIR, "static/img/", filename),
    'wb+') as uploaded_file:
    for chunk in file.chunks():
      uploaded_file.write(chunk)
  
  return filename