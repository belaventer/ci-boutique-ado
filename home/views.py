from django.shortcuts import render


def index(request):
    """
    View to retunr index page
    """
    return render(request, 'home/index.html')
