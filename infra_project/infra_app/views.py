from django.http import HttpResponse


def index(request):
    return HttpResponse('<center><b>У меня получилось!</b></center>')


def second_page(request):
    return HttpResponse('<strong>А это вторая страница</strong>')
