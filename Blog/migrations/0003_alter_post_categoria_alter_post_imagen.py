# Generated by Django 4.1.3 on 2022-12-27 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_alter_post_categoria_alter_post_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categoria',
            field=models.CharField(choices=[('Futbol', 'Futbol'), ('Juegos', 'Juegos'), ('Viajes', 'Viajes'), ('Salud', 'Salud'), ('Eventos', 'Eventos'), ('Varios', 'Varios')], default='VARIOS', max_length=9),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]