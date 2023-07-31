from django.shortcuts import render


def handler404(request, exception):
    """ERROR HANDLER 404 - PAGE NOT FOUND"""
    template = "errors/404.html"
    status = 404
    return render(request, template, status=status)
