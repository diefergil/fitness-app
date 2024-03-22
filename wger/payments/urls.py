# Django
from django.conf.urls import include
from django.urls import path

# wger
from wger.payments.views import subscription

pattern_payments = [path('payments', subscription.user_subscription, name='user_subscription')]

urlpatterns = [path('', include((pattern_payments, 'payments'), namespace='payments'))]
