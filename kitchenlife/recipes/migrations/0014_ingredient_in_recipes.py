# Generated by Django 4.1.6 on 2023-02-13 11:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0013_alter_ingredient_in_cupboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='in_recipes',
            field=models.ManyToManyField(blank=True, default='admin', related_name='owned_ingredient', to=settings.AUTH_USER_MODEL),
        ),
    ]
