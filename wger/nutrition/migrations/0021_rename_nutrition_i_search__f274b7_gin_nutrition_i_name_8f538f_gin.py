# Generated by Django 4.2.6 on 2024-03-26 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0020_full_text_search'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='ingredient',
            new_name='nutrition_i_name_8f538f_gin',
            old_name='nutrition_i_search__f274b7_gin',
        ),
    ]
