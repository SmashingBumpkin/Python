# Generated by Django 4.1.7 on 2023-03-30 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cupboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='category',
            field=models.CharField(blank=True, default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='substitutes',
            field=models.CharField(blank=True, default='', max_length=200),
            preserve_default=False,
        ),
    ]