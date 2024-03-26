# Django
from django.conf.urls import include
from django.urls import path

# wger
from wger.subscriptions.views import subscription, add_trainer

pattern_payments = [
    path('payments', subscription.user_subscription, name='user_subscription'),
    path('<int:user_pk>/add_trainer', add_trainer.add_trainer, name='add_trainer'),
]

urlpatterns = [path('', include((pattern_payments, 'payments'), namespace='payments'))]
