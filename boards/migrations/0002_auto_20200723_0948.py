# Generated by Django 3.0.8 on 2020-07-23 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='last_update',
            new_name='last_updated',
        ),
        migrations.AlterField(
            model_name='board',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(max_length=4000),
        ),
    ]
