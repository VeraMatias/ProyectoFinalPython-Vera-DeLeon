# Generated by Django 4.1.3 on 2023-01-02 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_alter_post_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categoria',
            field=models.CharField(choices=[('Futbol', 'Futbol'), ('Juegos', 'Juegos'), ('Viajes', 'Viajes'), ('Salud', 'Salud'), ('Eventos', 'Eventos'), ('Varios', 'Varios')], default='Varios', max_length=9),
        ),
    ]
