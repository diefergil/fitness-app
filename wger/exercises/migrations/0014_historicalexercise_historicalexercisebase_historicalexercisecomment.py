# Generated by Django 3.2.3 on 2021-05-30 14:24

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0012_auto_20210210_1228'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exercises', '0013_auto_20210503_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalExerciseComment',
            fields=[
                (
                    'id',
                    models.IntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name='ID'
                    )
                ),
                (
                    'comment',
                    models.CharField(
                        help_text='A comment about how to correctly do this exercise.',
                        max_length=200,
                        verbose_name='Comment'
                    )
                ),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                (
                    'history_type',
                    models.CharField(
                        choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')],
                        max_length=1
                    )
                ),
                (
                    'exercise',
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name='+',
                        to='exercises.exercise',
                        verbose_name='Exercise'
                    )
                ),
                (
                    'history_user',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='+',
                        to=settings.AUTH_USER_MODEL
                    )
                ),
            ],
            options={
                'verbose_name': 'historical exercise comment',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalExerciseBase',
            fields=[
                (
                    'id',
                    models.IntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name='ID'
                    )
                ),
                (
                    'license_author',
                    models.CharField(
                        blank=True,
                        help_text='If you are not the author, enter '
                        'the name or source here. This is '
                        'needed for some licenses e.g. the '
                        'CC-BY-SA.',
                        max_length=50,
                        null=True,
                        verbose_name='Author'
                    )
                ),
                (
                    'status',
                    models.CharField(
                        choices=[('1', 'Pending'), ('2', 'Accepted'), ('3', 'Declined')],
                        default='1',
                        editable=False,
                        max_length=2
                    )
                ),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='UUID')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                (
                    'history_type',
                    models.CharField(
                        choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')],
                        max_length=1
                    )
                ),
                (
                    'category',
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name='+',
                        to='exercises.exercisecategory',
                        verbose_name='Category'
                    )
                ),
                (
                    'history_user',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='+',
                        to=settings.AUTH_USER_MODEL
                    )
                ),
                (
                    'license',
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        default=2,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name='+',
                        to='core.license',
                        verbose_name='License'
                    )
                ),
                (
                    'variations',
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name='+',
                        to='exercises.variation',
                        verbose_name='Variations'
                    )
                ),
            ],
            options={
                'verbose_name': 'historical exercise base',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalExercise',
            fields=[
                (
                    'id',
                    models.IntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name='ID'
                    )
                ),
                (
                    'license_author',
                    models.CharField(
                        blank=True,
                        help_text='If you are not the author, enter the name or source '
                        'here. This is needed for some licenses e.g. the'
                        'CC-BY-SA.',
                        max_length=50,
                        null=True,
                        verbose_name='Author'
                    )
                ),
                (
                    'status',
                    models.CharField(
                        choices=[('1', 'Pending'), ('2', 'Accepted'), ('3', 'Declined')],
                        default='1',
                        editable=False,
                        max_length=2
                    )
                ),
                (
                    'description',
                    models.TextField(
                        max_length=2000,
                        validators=[django.core.validators.MinLengthValidator(40)],
                        verbose_name='Description'
                    )
                ),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                (
                    'name_original',
                    models.CharField(default='', max_length=200, verbose_name='Name')
                ),
                (
                    'creation_date',
                    models.DateField(blank=True, editable=False, null=True, verbose_name='Date')
                ),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='UUID')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                (
                    'history_type',
                    models.CharField(
                        choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')],
                        max_length=1
                    )
                ),
                (
                    'exercise_base',
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name='+',
                        to='exercises.exercisebase',
                        verbose_name='ExerciseBase'
                    )
                ),
                (
                    'history_user',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='+',
                        to=settings.AUTH_USER_MODEL
                    )
                ),
                (
                    'language',
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name='+',
                        to='core.language',
                        verbose_name='Language'
                    )
                ),
                (
                    'license',
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        default=2,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name='+',
                        to='core.license',
                        verbose_name='License'
                    )
                ),
            ],
            options={
                'verbose_name': 'historical exercise',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
