# Generated by Django 4.1.7 on 2023-03-08 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_rename_string_recipeingredient_local_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeingredient',
            name='alternative',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='optional',
            field=models.BooleanField(default=False),
        ),
    ]
