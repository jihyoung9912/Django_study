from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse('<h1>코스트랑 오픈!<h1>')

# Create your views here.
