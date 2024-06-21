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
            return redirect(to='profile')
    form = CustomUserForm()
    context = {
        'form':form,
    }
    return render(request, 'user/register.html', context)


def list_user(request):
    form = CustomUser.objects.all()
    context = {'form':form,}
    return render(request, 'user/list.html', context)


def edit_user(request, id):
    id_user = CustomUser.objects.get(id=id)
    form = CustomUserForm(request.POST or None, instance=id_user)
    if form.is_valid():
        form.save()
        return redirect(to='list')
    if request.method != 'POST':
        form = CustomUser(instance=id_user)
        context = {'form':form}
        return render(request, 'user/edit.html', context)


def delete_user(request, id):
    id_user = CustomUser.objects.get(id=id)
    id_user.delete()
    return redirect(to='list')


def create_profile(request):
    if request.method == 'POST':
        form = ProfileUser(request.POST or None)
        if form.is_valid():
            form.save()
    form = ProfileUser()
    context = {'form':form,}
    return render(request, 'profile/create.html', context)