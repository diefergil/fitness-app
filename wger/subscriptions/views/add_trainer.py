# Standard Library
import logging


from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.http.response import (
    HttpResponseForbidden,
)
from django.shortcuts import (
    get_object_or_404,
    render,
)
from wger.subscriptions.forms import TrainerFormRecaptcha

logger = logging.getLogger(__name__)




@login_required
def add_trainer(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)

    if request.method == 'POST':
        form = TrainerFormRecaptcha(request.POST, instance=user)
        if form.is_valid():
            form.save()
            logger.info('Your user is now a trainer')
            # Redirect to a success page or similar
    else:
        form = TrainerFormRecaptcha(instance=user)

    context = {'form': form, 'user': user}
    return render(request, 'trainer_data.html', context)
