from django.shortcuts import render
from app.models import Car

# Create your views here.
def index(request):
  list = Car.objects.all()
  return render(request, 'index.html', {'list': list})

