from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.forms import ProfileForm
from accounts.models import Profile


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


@login_required
def profile_edit(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'accounts/profile_form.html', {
        'form': form,
    })