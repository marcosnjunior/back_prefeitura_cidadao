# Generated by Django 5.1 on 2024-08-23 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("licenciamento_2", "0016_atualizacao_cadatral_dos_quiosques_descricao_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="atualizacao_cadatral_dos_quiosques",
            name="Tempo_Ocupa",
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name="atualizacao_cadatral_dos_quiosques",
            name="Validade_Permissao",
            field=models.CharField(default=None, max_length=100),
        ),
    ]
