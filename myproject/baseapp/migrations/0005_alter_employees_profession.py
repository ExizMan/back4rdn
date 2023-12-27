# Generated by Django 4.2.5 on 2023-12-27 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0004_professions_employees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='profession',
            field=models.ForeignKey(default='без должности', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='employees', to='baseapp.professions'),
        ),
    ]
