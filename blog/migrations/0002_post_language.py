# Generated by Django 4.2.4 on 2023-08-09 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='language',
            field=models.CharField(choices=[('MR', 'Marathi'), ('EN', 'English')], default='MR', max_length=2, verbose_name='language'),
        ),
    ]
