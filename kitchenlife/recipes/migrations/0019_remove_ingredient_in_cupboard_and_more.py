# Generated by Django 4.1.6 on 2023-02-14 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0018_profile_delete_cupboard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='in_cupboard',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='in_recipes',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='profile',
            name='ingredients_owned',
            field=models.ManyToManyField(related_name='owned_by_profile', to='recipes.ingredient'),
        ),
        migrations.AddField(
            model_name='profile',
            name='ingredients_referenced',
            field=models.ManyToManyField(related_name='referenced_by_profile', to='recipes.ingredient'),
        ),
    ]
