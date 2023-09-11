# Generated by Django 4.2.4 on 2023-09-10 03:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_township_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='township-image')),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('township', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.township')),
            ],
        ),
    ]