from django.shortcuts import render

# Create your views here.
def resume(request):
    context={
    }
    return render(request, 'resume.html', context)