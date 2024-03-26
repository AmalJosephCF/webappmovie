from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from credentialsapp.forms import userForm


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/movieapp')


def login(request):
    if request.method == 'POST':
        uname = request.POST["username"]
        pwd = request.POST["password"]
        user1 = auth.authenticate(username=uname, password=pwd)
        if user1 is not None:
            auth.login(request, user1)
            return redirect('/movieapp')
        else:
            messages.info(request, "Invalid user")


    return render(request, 'login.html')


def registrations(request):
    if request.method == 'POST':
        uname = request.POST["username"]
        fname = request.POST["firstname"]
        sname = request.POST["secondname"]
        mail = request.POST["email"]
        pwd = request.POST["password"]
        cpswd = request.POST["confirmpaswword"]
        if uname==''or fname==''or sname==''or mail==''or pwd=='':
            messages.info(request, "Please eneter the values!")
            return render(request, 'registration.html')
            # return redirect('registrations')
        if pwd == cpswd:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "User already exists")
                return redirect('registrations')
            elif User.objects.filter(email=mail).exists():
                messages.info(request, "Email id already exists")
                return redirect('registrations')
            else:
                userInfo = User.objects.create_user(username=uname, password=pwd, first_name=fname, last_name=sname,
                                                    email=mail)
                userInfo.save()
                # messages.info(request, "Profile created sucessfully!")
                return render(request, 'registration.html', {'profile_created': True})
                print("user created")

        else:

            print("password not matching")
            messages.info(request, "Password not matching")
            return redirect('registrations')
            messages.info(request,'')
        return redirect('/movieapp')
    return render(request, "registration.html")


def updateProfile(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user_form = userForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('/movieapp')
    else:
        user_form = userForm(instance=user)

    return render(request, 'update.html', {'user_form': user_form, 'user': user})