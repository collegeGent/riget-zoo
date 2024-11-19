from django.shortcuts import render

# Create your views here.
def home(request):
    context={'bgImage': 'tiger.jpg',}
    return render(request, 'pages/index.html', context=context)