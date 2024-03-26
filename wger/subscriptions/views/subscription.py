# Standard Library
import logging

# Third Party
import stripe

# Django
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import csrf
from django.urls import reverse

# wger
from wger.subscriptions.forms import PaymentForm


logger = logging.getLogger(__name__)


@login_required
def user_subscription(request):
    context = {}
    context.update(csrf(request))
    stripe.api_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        if 'subscribe' in request.POST:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price': settings.PRICE_BASIC_SUBSCRIPTION,
                        'quantity': 1,
                    },
                ],
                mode='subscription',
                success_url=settings.SITE_URL
                + '/payment_successful?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=settings.SITE_URL + '/payment_cancelled',
            )
            return HttpResponseRedirect(checkout_session.url, status=303)
        elif 'access_free' in request.POST:
            # Redirect the user to an internal page for free features
            return HttpResponseRedirect(
                reverse('subscriptions:payments:add_trainer', kwargs={'user_pk': request.user.pk})
            )

    return render(request, 'payments/user_subscription.html', context)
