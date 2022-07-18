from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, logout_then_login
from accounts.forms import UserForm
from accounts.models import User


login = LoginView.as_view(template_name='accounts/index.html')


def logout(request):
    return logout_then_login(request)


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


@login_required
def profile_edit(request):
    try:
        profile = request.user.username
    except User.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = UserForm(instance=profile)
    return render(request, 'accounts/profile_form.html', {
        'form': form,
    })