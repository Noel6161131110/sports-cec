from django.shortcuts import render


def dash(request):
    return render(request , "dash.html")