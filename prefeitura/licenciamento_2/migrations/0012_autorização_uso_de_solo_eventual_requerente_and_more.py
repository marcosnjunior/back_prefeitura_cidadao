# Generated by Django 5.1 on 2024-08-23 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("licenciamento_2", "0011_alter_sedrub_endereco_alter_sedrub_requerente"),
    ]

    operations = [
        migrations.AddField(
            model_name="autorização_uso_de_solo_eventual",
            name="Requerente",
            field=models.CharField(default="Nome", max_length=200),
        ),
        migrations.AlterField(
            model_name="autorização_uso_de_solo_eventual",
            name="Endereco",
            field=models.CharField(max_length=500),
        ),
    ]
