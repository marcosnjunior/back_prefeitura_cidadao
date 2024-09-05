# Generated by Django 5.0 on 2024-08-08 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animais", "0002_apreensaoanimal"),
    ]

    operations = [
        migrations.CreateModel(
            name="Denuncia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("relatoDenuncia", models.CharField(max_length=200)),
                ("cep", models.CharField(blank=True, max_length=40)),
                ("bairro", models.CharField(max_length=100)),
                ("rua", models.CharField(max_length=200)),
                ("pontoRef", models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name="apreensaoanimal",
            name="bairro",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="apreensaoanimal",
            name="cep",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="apreensaoanimal",
            name="cidade",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="apreensaoanimal",
            name="estado",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="apreensaoanimal",
            name="numero",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="apreensaoanimal",
            name="pontoRef",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="apreensaoanimal",
            name="rua",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="coletaanimaismortos",
            name="animal_de_grande_porte",
            field=models.CharField(
                choices=[
                    ("Cavalo", "Cavalo"),
                    ("Boi", "Boi"),
                    ("Cabra", "Cabra"),
                    ("Porco", "Porco"),
                ],
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="coletaanimaismortos",
            name="bairro",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="coletaanimaismortos",
            name="cep",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="coletaanimaismortos",
            name="cidade",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="coletaanimaismortos",
            name="estado",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="coletaanimaismortos",
            name="numero",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="coletaanimaismortos",
            name="pontoRef",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="coletaanimaismortos",
            name="rua",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
