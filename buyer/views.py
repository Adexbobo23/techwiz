from django.shortcuts import render

def buyer_dashboard(request):
    return render(request, 'buyer/index.html')