from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from . import forms

# Home Page functions


def home_view(request):
    return render(request, 'home/index.html')

# Registration


def usersignup_view(request):
    form1 = forms.UserForm()
    mydict = {'form1': form1}
    if request.method == 'POST':
        form1 = forms.UserForm(request.POST)
        if form1.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            # my_student_group = Group.objects.get_or_create(name='STUDENT')
            # my_student_group[0].user_set.add(user)
        return HttpResponseRedirect('userlogin')
    return render(request, 'regist/usersignup.html', context=mydict)


def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()

# After Login function
def afterlogin_view(request):
    print(is_admin(request.user))
    if is_admin(request.user):
        return render(request, 'home/index.html')
    else:
        return render(request, 'home/index.html')
