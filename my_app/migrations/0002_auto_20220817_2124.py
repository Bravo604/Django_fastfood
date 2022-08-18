# Generated by Django 3.2 on 2022-08-17 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='email',
        ),
        migrations.AddField(
            model_name='food',
            name='clients',
            field=models.ManyToManyField(through='my_app.Order', to='my_app.Client'),
        ),
        migrations.AddField(
            model_name='food',
            name='workers',
            field=models.ManyToManyField(through='my_app.Order', to='my_app.Worker'),
        ),
    ]
