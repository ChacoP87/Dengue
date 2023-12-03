# Generated by Django 4.2.7 on 2023-11-28 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hemorragicos', models.BooleanField()),
                ('diabetes', models.BooleanField()),
                ('hipertension', models.BooleanField()),
                ('ENFERMEDAD_ULC_PEPTICA', models.BooleanField()),
                ('ENFERMEDAD_RENAL', models.BooleanField()),
                ('INMUNOSUPR', models.BooleanField()),
                ('CIRROSIS_HEPATICA', models.BooleanField()),
                ('DEFUNCION', models.BooleanField()),
            ],
        ),
    ]
