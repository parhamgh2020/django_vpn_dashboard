from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.shortcuts import redirect, render

from .forms import SignupForm, MessageForm, LoginForm


def home(request):
    template_name = 'home.html'
    context = {}
    if request.method == 'GET':
        return render(request, template_name, context)


def contact(request):
    template_name = 'contact.html'
    context = {}
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/home/')
    else:
        form = MessageForm()
        context['form'] = form

    return render(request, template_name, context)


def signup(request):
    template_name = 'signup.html'
    context = {}
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
        context['form'] = form

    return render(request, template_name, context)


def logout_view(request):
    logout(request)
    return redirect('')


def login(request):
    template_name = 'login.html'
    context = {}
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard:dashboard")
    context = {'form': form}
    return render(request, 'login.html', context=context)


@login_required(login_url='base:login')
def profile(request):
    template_name = 'profile.html'
    context = {}
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/profile/')
    else:
        form = SignupForm()
        context['form'] = form

    return render(request, template_name, context)

# @login_required(login_url='my-login')
# def profile_management(request):
#     user_form = UpdateUserForm(instance=request.user)
#     profile = Profile.objects.get(user=request.user)
#     profile_form = UpdateProfileForm(instance=profile)
#
#     if request.method == 'POST':
#         user_form = UpdateUserForm(request.POST, instance=request.user)
#         profile_form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
#         if user_form.is_valid():
#             user_form.save()
#             return redirect("dashboard")
#         if profile_form.is_valid():
#             profile_form.save()
#             return redirect("dashboard")
#
#     context = {'user_form': user_form, 'profile_form': profile_form}
#     return render(request, 'lynx/profile-management.html', context=context)
#
#
# @login_required(login_url='my-login')
# def delete_account(request):
#     if request.method == "POST":
#         deleteUser = User.objects.get(username=request.user)
#         deleteUser.delete()
#         return redirect("")
#     return render(request, 'lynx/delete-account.html')
#
