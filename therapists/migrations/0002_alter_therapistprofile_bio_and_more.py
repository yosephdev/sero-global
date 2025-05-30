# Generated by Django 5.2.1 on 2025-05-20 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='therapistprofile',
            name='bio',
            field=models.TextField(blank=True, verbose_name='bio'),
        ),
        migrations.AlterField(
            model_name='therapistprofile',
            name='hourly_rate',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='hourly rate'),
        ),
        migrations.AlterField(
            model_name='therapistprofile',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='is available'),
        ),
        migrations.AlterField(
            model_name='therapistprofile',
            name='license_number',
            field=models.CharField(max_length=50, unique=True, verbose_name='license number'),
        ),
        migrations.AlterField(
            model_name='therapistprofile',
            name='specialization',
            field=models.CharField(choices=[('clinical', 'Clinical Psychology'), ('counseling', 'Counseling Psychology'), ('forensic', 'Forensic Psychology'), ('health', 'Health Psychology'), ('neuro', 'Neuropsychology'), ('school', 'School Psychology')], default='clinical', max_length=20, verbose_name='specialization'),
        ),
        migrations.AlterField(
            model_name='therapistprofile',
            name='years_of_experience',
            field=models.PositiveIntegerField(default=0, verbose_name='years of experience'),
        ),
    ]
