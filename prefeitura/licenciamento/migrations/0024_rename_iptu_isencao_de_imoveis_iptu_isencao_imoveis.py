# Generated by Django 5.1 on 2024-08-23 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("licenciamento", "0023_rename_iptu_isencao_imoveis_iptu_isencao_de_imoveis"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="IPTU_Isencao_de_Imoveis",
            new_name="IPTU_Isencao_Imoveis",
        ),
    ]
