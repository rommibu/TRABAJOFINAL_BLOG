# Generated by Django 4.0.5 on 2022-09-01 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMVT', '0002_rename_fecha_afiliacion_coberturasalud_fecha_creacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('escuderias', models.CharField(choices=[('Ferrari', 'Ferrari'), ('Mercedes', 'Mercedes'), ('Alpine', 'Alpine'), ('Haas', 'Haas'), ('Alfa Romeo', 'Alfa Romeo'), ('Aston Martin', 'Aston Martin'), ('Alphatauri', 'Alphatauri'), ('Williams', 'Williams'), ('Red Bull', 'Red Bull'), ('Mclaren', 'Mclaren')], default='Alfa Romeo', max_length=30)),
                ('piloto', models.IntegerField()),
            ],
        ),
    ]
