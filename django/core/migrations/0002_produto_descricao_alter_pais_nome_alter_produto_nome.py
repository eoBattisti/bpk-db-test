# Generated by Django 4.0.3 on 2023-05-28 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='descricao',
            field=models.CharField(default=0, max_length=200, verbose_name='Nome'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pais',
            name='nome',
            field=models.TextField(max_length=255, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
    ]