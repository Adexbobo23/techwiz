from django.shortcuts import render

def home(request):
    return render(request, 'front-end/index.html')