from django.http import HttpResponse


def index(request):
    return HttpResponse("<html><body><center><b>У меня получилось!</b></center></body></html>")


def second_page(request):
    return HttpResponse("<html><body><strong>А это вторая страница</strong></body></html>")
