from django.shortcuts import render

# Create your views here.
def index_cv(request):
    return render(
        request,
        'cv/cv.html'
    )