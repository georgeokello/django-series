from django.shortcuts import render
from . models import Data


def home(request):

    user_data = Data.objects.all()

    return render(request, 'index.html', {'user_data':user_data})