# Generated by Django 5.1 on 2024-08-22 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("licenciamento", "0004_alter_sedrub_descricao_alter_sedrub_endereco"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sedrub",
            name="CPF",
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name="sedrub",
            name="Requerente",
            field=models.TextField(default=None),
        ),
    ]
