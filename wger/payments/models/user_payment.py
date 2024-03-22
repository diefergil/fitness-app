# Django
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserPayment(models.Model):
    user = models.ForeignKey(
        User,
        editable=False,
        on_delete=models.CASCADE,
    )
    payment_bool = models.BooleanField(default=False)
    stripe_checkout_id = models.CharField(max_length=500, blank=True, null=True)


@receiver(post_save, sender=User)
def create_user_payment(sender, instance, created, **kwargs):
    if created:
        UserPayment.objects.create(user=instance)
