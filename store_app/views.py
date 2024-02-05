from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import auth
from . forms import user_profile_form
from django.contrib.auth import authenticate, login
from . forms import registration_form
from django.contrib.auth.forms import AuthenticationForm
from . models import Course, User_profile
from django.contrib.auth.decorators import login_required
# Create your views here.


#home_page
def home(request):
    return render(request, 'home.html')


#registration_page
def register_user(request):
    if request.method == 'POST':
        form = registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_user')
    else:
        form = registration_form()
    context = {'form': form,}
    return render(request, 'register_user.html', context)


# login_page
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            profile = authenticate(request, username=username, password=password)
            if profile is not None:
                login(request, profile)
                return redirect('landing_page')
    else:
        form = AuthenticationForm()
    context = {'form': form,}
    return render(request, 'login_user.html', context)


# landing_page after user login
@login_required(login_url='login_user')
def landing_page(request):
    details = User_profile.objects.filter(user=request.user)
    context = {'details': details}
    return render(request, 'landing_page.html', context)


# user details form
@login_required(login_url='login_user')
def user_profile(request):
    if request.method == 'POST':
        form = user_profile_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('order_confirmation')

    else:
        form = user_profile_form()
    context = {'form': form, }

    return render(request, 'user_profile.html', context)


# logout
def logout(request):
    auth.logout(request)
    return redirect('home')


# Ajax load_courses
def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).values('id', 'course')
    return JsonResponse(list(courses), safe=False)


# Order confirmation page
@login_required(login_url='login_user')
def order_confirmation(request):
    return render(request, 'order_confirmation.html')