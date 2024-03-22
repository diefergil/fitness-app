# Django
# Third Party
import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import csrf

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
                    'price': settings.PRODUCT_PRICE,
                    'quantity': 1,
                },
            ],
            mode='payment',
            customer_creation='always',
            success_url=settings.REDIRECT_DOMAIN
            + '/payment_susccesful?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=settings.REDIRECT_DOMAIN + '/payment_cancelled',
        )
        # form = PaymentForm(request.POST)
        return HttpResponseRedirect(checkout_session.url, status_code=303)

    else:
        data = {
            'payment_method': 'credit_card',
            'credit_card_number': '1234 5678 9012 3456',
            'cvv': '123',
            'expiration_date': '12/2022',
        }

    form = PaymentForm(initial=data)
    context['form'] = form

    return render(request, 'payments/user_payment.html', context)
