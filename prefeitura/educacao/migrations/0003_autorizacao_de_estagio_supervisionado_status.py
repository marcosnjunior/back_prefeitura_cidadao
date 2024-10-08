# Generated by Django 5.0 on 2024-09-05 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "educacao",
            "0002_alter_autorizacao_de_estagio_supervisionado_options_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="autorizacao_de_estagio_supervisionado",
            name="status",
            field=models.CharField(
                choices=[
                    ("ABERTO", "Aberto"),
                    ("ANDAMENTO", "Em Andamento"),
                    ("FECHADO", "Fechado"),
                ],
                default="Aberto",
                max_length=30,
            ),
        ),
    ]
