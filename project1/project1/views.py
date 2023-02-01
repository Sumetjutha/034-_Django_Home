from django.http import HttpResponse


def index(request):
    return HttpResponse('Welcome to my homepage')


def about(request):
    return HttpResponse('This is a test of Django framework')


def book_python(request):
    return HttpResponse('การเขียนโปรแกรมด้วย Python สำหรับผู้เริ่มต้น')


def dj_ch01(request):
    return HttpResponse('Django Chapter 1: Initial Setup')
