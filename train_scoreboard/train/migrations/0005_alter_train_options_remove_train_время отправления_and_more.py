# Generated by Django 4.0.4 on 2022-05-16 13:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0004_rename_задержан_train_задержан до_alter_train_статус'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='train',
            options={'ordering': ['departure_time'], 'verbose_name': 'Поезд', 'verbose_name_plural': 'Поезда'},
        ),
        migrations.RemoveField(
            model_name='train',
            name='Время отправления',
        ),
        migrations.RemoveField(
            model_name='train',
            name='Время прибытия',
        ),
        migrations.RemoveField(
            model_name='train',
            name='Город отправления',
        ),
        migrations.RemoveField(
            model_name='train',
            name='Город прибытия',
        ),
        migrations.RemoveField(
            model_name='train',
            name='Задержан до',
        ),
        migrations.RemoveField(
            model_name='train',
            name='Номер платформы',
        ),
        migrations.RemoveField(
            model_name='train',
            name='Статус',
        ),
        migrations.AddField(
            model_name='train',
            name='arrival_city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='arrival_city', to='train.city', verbose_name='Город прибытия'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='train',
            name='arrival_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время прибытия'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='train',
            name='departure_city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='departure_city', to='train.city', verbose_name='Город отправления'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='train',
            name='departure_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время отправления'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='train',
            name='detained_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Задержан до'),
        ),
        migrations.AddField(
            model_name='train',
            name='platform_number',
            field=models.IntegerField(default=1, verbose_name='Номер платформы'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='train',
            name='status',
            field=models.CharField(choices=[(None, 'Выберите статус'), ('l', 'Идет посадка'), ('a', 'Прибытие'), ('s', 'Отправлен'), ('d ', 'Задержан'), ('c ', 'Отменен')], default=1, max_length=255, verbose_name='Статус'),
            preserve_default=False,
        ),
    ]
