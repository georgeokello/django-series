from django.shortcuts import render
from . models import Data
from . forms import OurForm


def home(request):

    user_data = Data.objects.all()

    if request.method == 'POST':
        form = OurForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OurForm()
    return render(request, 'index.html', {'user_data':user_data, 'form':form})