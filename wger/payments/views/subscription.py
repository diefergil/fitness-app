# Django
# Third Party
import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import csrf
from django.shortcuts import redirect

from wger.payments.forms import PaymentForm


@login_required
def user_subscription(request):
    """
    View to render and process the payment form.
    """
    context = {}
    context.update(csrf(request))
    stripe.api_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': settings.PRICE_BASIC_SUBSCRIPTION,
                    'quantity': 1,
                },
            ],
            mode='subscription',
            success_url=settings.SITE_URL + '/payment_susccesful?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=settings.SITE_URL + '/payment_cancelled',
        )
        # form = PaymentForm(request.POST)
        return HttpResponseRedirect(checkout_session.url, status=303)

    # form = PaymentForm(initial=data)
    # context['form'] = form

    return render(request, 'payments/user_subscription.html', context)
