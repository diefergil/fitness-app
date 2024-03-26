import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def set_default_gym_owner(apps, schema_editor):
    Gym = apps.get_model('gym', 'Gym')

    for gym in Gym.objects.all():
            gym.owner = 1 # assign current gyms to the admin
            gym.save()


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gym', '0008_auto_20190618_1617'),
    ]

    operations = [
        migrations.RunPython(set_default_gym_owner, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='gym',
            name='owner',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='owned_gyms',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Owner',
            ),
        ),
    ]
