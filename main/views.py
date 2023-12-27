from django.shortcuts import render
from .models import Image
from .forms import ImageForm


def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    

    form = ImageForm
    images = Image.objects.all()
    data = {
        'form':form,
        'images' : images
    }
    return render(request, "home.html",data)
