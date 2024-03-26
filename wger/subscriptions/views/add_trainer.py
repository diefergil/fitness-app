# Standard Library
import logging

# Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.http.response import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

# wger
from wger.subscriptions.forms import GymForm
from wger.gym.models import Gym

logger = logging.getLogger(__name__)


@login_required
def add_trainer(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    user_gyms = Gym.objects.filter(owner=user)

    # Check if the user's email is verified
    if not user.userprofile.email_verified:
        return HttpResponseForbidden('Your email address must be verified to create a gym.')

    # Check if the user already has a gym
    if user_gyms.count() >= 1:
        return HttpResponseForbidden('You cannot create more than one gym.')

    if request.method == 'POST':
        form = GymForm(request.POST, user=request.user)
        if form.is_valid():
            new_gym = form.save(commit=False)
            new_gym.owner = user  # Set the gym's owner to the current user
            new_gym.save()

            # Ensure the user's profile is associated with the gym
            user_profile = user.userprofile
            user_profile.gym = new_gym
            user_profile.save()

            # Add user to gym-related groups
            user.groups.add(Group.objects.get(name='gym_member'))
            user.groups.add(Group.objects.get(name='gym_trainer'))
            user.groups.add(Group.objects.get(name='gym_manager'))

            return HttpResponseRedirect(reverse('gym:gym:user-list', kwargs={'pk': new_gym.pk}))
    else:
        form = GymForm(user=request.user)

    context = {'form': form, 'user': user}
    return render(request, 'trainer_data.html', context)
