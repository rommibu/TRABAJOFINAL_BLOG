# Generated by Django 4.1 on 2022-09-28 15:51

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('DM', '0002_canal_canalusuario_menssage_delete_mensaje_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='canal',
            managers=[
                ('ojects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='canalmensaje',
            name='texto',
            field=models.TextField(default='texto'),
        ),
    ]
