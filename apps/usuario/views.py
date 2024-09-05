from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser, ProfileUser
from .forms import CustomUserForm, ProfileUserForm


def home(request):
    return render(request, 'user/index.html', {})


def register_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(to='detail-profile')
    form = CustomUserForm()
    context = {
        'form':form,
    }
    return render(request, 'registration/register.html', context)


def list_user(request):
    form = CustomUser.objects.all()
    context = {'form':form,}
    return render(request, 'user/list.html', context)


def edit_user(request, id):
    id_user = CustomUser.objects.get(id=id)
    form = CustomUserForm(request.POST or None, instance=id_user)
    if form.is_valid():
        form.save()
        return redirect(to='list-user')
    if request.method != 'POST':
        form = CustomUserForm(instance=id_user)
        context = {'form':form, 'id_user':id_user}
        return render(request, 'user/edit.html', context)


def delete_user(request, id):
    id_user = CustomUser.objects.get(id=id)
    id_user.delete()
    return redirect(to='list-user')


def detail_profile(request, id):
    id_profile = ProfileUser(id=id)
    form = ProfileUserForm()
    context = {
        'form':form,
        'id_profile':id_profile}
    return render(request, 'profile/detail.html', context)


def edit_profile(request):
    """ id_profile = ProfileUser.objects.get(id=id) """
    form_user = CustomUserForm(request.POST or None, instance=request.user)
    form_profile = ProfileUserForm(request.POST, request.FILES, instance=request.user.profile)
    if form_profile.is_valid() and form_user.is_valid():
        form_profile.save()
        form_user.save()
        return redirect(to='detail-profile')
    if request.method != 'POST':
        form_user = CustomUserForm(instance=request.user)
        form_profile = ProfileUserForm(instance=request.user.profile)
        context = {
            'form_profile':form_profile,
            'form_user':form_user,
        }
        return render(request, 'profile/edit_profile.html', context)


def delete_profile(request, id):
    id_profile = ProfileUser.objects.get(id=id)
    id_profile.delete()
    return redirect(to='home')