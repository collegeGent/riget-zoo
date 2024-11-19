from django.shortcuts import render

# Create your views here.
def home(request):
    webpage = 'pages/index.html'
    context={'bgImage': 'tiger.jpg',}
    return render(request, webpage, context=context)


def example(request):

        return render(request, "example/parent.html")
