# Generated by Django 3.2.5 on 2022-01-03 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('spended_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
