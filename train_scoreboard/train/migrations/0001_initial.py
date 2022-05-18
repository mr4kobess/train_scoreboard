# Generated by Django 4.0.4 on 2022-05-16 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Наименование', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Номер', models.IntegerField()),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('Номер платформы', models.IntegerField()),
                ('Статус', models.CharField(max_length=255)),
                ('Город отправления', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_city', to='train.city')),
                ('Город прибытия', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_city', to='train.city')),
            ],
        ),
    ]