from django.shortcuts import render

from .models import Feedback


def index(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        feedback=Feedback(name=name,email=email,message=message)
        feedback.save()
    return render(request, 'index.html')