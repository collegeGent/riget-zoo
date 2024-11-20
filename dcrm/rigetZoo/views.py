from django.shortcuts import render

# Create your views here.
def home(request):
    webpage = 'pages/index.html'
    context={'bgImage': 'tiger.jpg',}
    return render(request, webpage, context=context)

def visitUs(request):
    webpage = 'pages/visitUs.html'
    context={'bgImage': 'parrot.jpg',}
    return render(request, webpage, context=context)

def visitEdu(request):
    webpage = 'pages/visitEdu.html'
    context={'bgImage': 'schoolVisit.jpg',}
    return render(request, webpage, context=context)

def whatsHere(request):
    webpage = 'pages/whatsHere.html'
    context={'bgImage': 'parkEntrance.jpg',}
    return render(request, webpage, context=context)

def aboutUs(request):
    webpage = 'pages/aboutUs.html'
    context={'bgImage': 'teamphoto.jpg',}
    return render(request, webpage, context=context)

def example(request):

        return render(request, "example/parent.html")
