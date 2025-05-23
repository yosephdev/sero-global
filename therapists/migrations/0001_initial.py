# Generated by Django 5.2.1 on 2025-05-20 13:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TherapistProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(choices=[('clinical', 'Clinical Psychology'), ('counseling', 'Counseling Psychology'), ('forensic', 'Forensic Psychology'), ('health', 'Health Psychology'), ('neuro', 'Neuropsychology'), ('school', 'School Psychology')], default='clinical', max_length=20)),
                ('license_number', models.CharField(max_length=50, unique=True)),
                ('years_of_experience', models.PositiveIntegerField(default=0)),
                ('bio', models.TextField(blank=True)),
                ('hourly_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='therapist_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Therapist Profile',
                'verbose_name_plural': 'Therapist Profiles',
            },
        ),
    ]
