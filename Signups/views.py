from django.shortcuts import render, redirect
from .models import Signups
from django.core.mail import send_mail
# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        useraname = request.POST['usernames']
        useremail = request.POST['useremails']
        userimage = request.FILES['userimages']
        password = request.POST['passwords']
        
        new_user = Signups(username=useraname, useremail=useremail, userimage = userimage, password= password)
        new_user.save()
        return redirect("/")
    context = {
        "title" : "Instagram - Signup"
    }
    return render(request, "registration/registration_form.html", context)