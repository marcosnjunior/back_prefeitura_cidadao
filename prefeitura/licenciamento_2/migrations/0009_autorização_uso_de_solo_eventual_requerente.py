# Generated by Django 5.1 on 2024-08-23 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "licenciamento_2",
            "0008_remove_autorização_uso_de_solo_eventual_requerente_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="autorização_uso_de_solo_eventual",
            name="Requerente",
            field=models.TextField(default=None),
        ),
    ]
