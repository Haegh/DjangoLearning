# Generated by Django 2.2.5 on 2019-09-26 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_url', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='miniurl',
            options={'verbose_name': 'Mini URL', 'verbose_name_plural': 'Minis URL'},
        ),
        migrations.RenameField(
            model_name='miniurl',
            old_name='url_field',
            new_name='url',
        ),
        migrations.AlterField(
            model_name='miniurl',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date de création'),
        ),
    ]
