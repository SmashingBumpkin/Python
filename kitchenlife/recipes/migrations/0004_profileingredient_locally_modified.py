# Generated by Django 4.1.7 on 2023-03-30 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_rename_ingredient_recipeingredient_profile_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileingredient',
            name='locally_modified',
            field=models.BooleanField(default=False),
        ),
    ]
