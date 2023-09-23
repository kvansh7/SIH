# Generated by Django 4.2.5 on 2023-09-23 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aptitude_test', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userscore',
            name='section',
        ),
        migrations.AddField(
            model_name='userscore',
            name='question',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='aptitude_test.question'),
            preserve_default=False,
        ),
    ]