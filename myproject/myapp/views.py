from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def cotton(request):
    return render(request, 'myapp/cotton.html')

# Аналогично для других тканей
def silk(request):
    return render(request, 'myapp/silk.html')

def wool(request):
    return render(request, 'myapp/wool.html')

def linen(request):
    return render(request, 'myapp/linen.html')