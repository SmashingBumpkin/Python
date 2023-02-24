# Generated by Django 4.1.6 on 2023-02-24 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mealplan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiscItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='misc_item', to='mealplan.mealplan')),
            ],
        ),
    ]
