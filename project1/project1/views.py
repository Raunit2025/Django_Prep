from django.http import HttpResponse

def handler404(request, exception):
    return HttpResponse("<h1>The page is not here </h2>",status=404)