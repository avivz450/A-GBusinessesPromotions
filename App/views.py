from django.shortcuts import render


# Create your views here.
def landingpage(request):
    return render(request, 'home/landingpage.html')


def base(request):
    return render(request, 'home/base.html')
