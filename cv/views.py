from django.shortcuts import render

# Create your views here.
def inicio_cv(request):
    return render(
        request,
        'cv/cv.html'
    )