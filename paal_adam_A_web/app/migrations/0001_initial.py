# Generated by Django 4.2.1 on 2023-05-31 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategorianev', models.CharField(max_length=50, verbose_name='kategorianev')),
            ],
        ),
        migrations.CreateModel(
            name='Teszt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kerdes', models.CharField(max_length=50, verbose_name='kerdes')),
                ('v1', models.CharField(max_length=50, verbose_name='valasz1')),
                ('v2', models.CharField(max_length=50, verbose_name='valasz2')),
                ('v3', models.CharField(max_length=50, verbose_name='valasz3')),
                ('v4', models.CharField(max_length=50, verbose_name='valasz4')),
                ('kategoriaID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.kategoria', verbose_name='kategoria_id_kulsokulcs')),
            ],
        ),
    ]
