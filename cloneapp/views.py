from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.

def index(request):
    return render(request, 'index.html')

def hire(request):
    if request.method == 'POST':
    
        first_name = request.POST['first_name']
        email = request.POST['email']
        message = request.POST['message']

        user = User.objects.create_user(first_name=first_name, email=email, message=message)
        user.save()
        print('thankYou')
        return redirect('/')

    else:
        return render(request, 'hire.html')