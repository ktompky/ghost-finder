from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello ghosties, let's get spooky.")

# Create your views here.
