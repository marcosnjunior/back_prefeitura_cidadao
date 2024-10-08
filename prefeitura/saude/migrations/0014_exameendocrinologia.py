# Generated by Django 5.0 on 2024-08-09 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("saude", "0013_alter_remedioemcasa_numerocns"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExameEndocrinologia",
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
                ("nome", models.CharField(max_length=100)),
                ("nomeRegistro", models.CharField(max_length=100)),
                ("telefone", models.CharField(max_length=15)),
                ("cidade", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("endereco", models.CharField(max_length=100)),
                ("dataNascimento", models.DateField()),
                (
                    "identidadeGenero",
                    models.CharField(
                        choices=[
                            ("F", "Feminino"),
                            ("M", "Masculino"),
                            ("NB", "Não-Binário"),
                            ("MC", "Mulher Cis"),
                            ("HC", "Homem Cis"),
                            ("MT", "Mulher Trans"),
                            ("HT", "Homem Trans"),
                            ("T", "Travesti"),
                            ("O", "Outro"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "orientacaoSexual",
                    models.CharField(
                        choices=[
                            ("F", "Feminino"),
                            ("M", "Masculino"),
                            ("NB", "Não-Binário"),
                            ("MC", "Mulher Cis"),
                            ("HC", "Homem Cis"),
                            ("MT", "Mulher Trans"),
                            ("HT", "Homem Trans"),
                            ("T", "Travesti"),
                            ("O", "Outro"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "cor",
                    models.CharField(
                        choices=[
                            ("B", "Branco"),
                            ("P", "Preto"),
                            ("I", "Indígena"),
                            ("A", "Amarelo"),
                            ("Q", "Quilombola"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "estadoCivil",
                    models.CharField(
                        choices=[
                            ("S", "Solteiro"),
                            ("C", "Casado"),
                            ("D", "Divorciado"),
                            ("V", "Viúvo"),
                            ("U", "União Estável"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "localViolencia",
                    models.CharField(
                        choices=[
                            ("D", "Domicílio"),
                            ("T", "Trabalho"),
                            ("E", "Escola"),
                            ("R", "Rua"),
                            ("O", "Outro"),
                        ],
                        max_length=1,
                    ),
                ),
                ("cpf", models.CharField(max_length=14)),
                (
                    "temDeficiencia",
                    models.CharField(
                        choices=[("S", "Sim"), ("N", "Não")], max_length=1
                    ),
                ),
                (
                    "tipoDeficiencia",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("F", "Física"),
                            ("M", "Mental"),
                            ("A", "Auditiva"),
                            ("V", "Visual"),
                            ("O", "Outra"),
                        ],
                        max_length=2,
                        null=True,
                    ),
                ),
                (
                    "recebeBeneficio",
                    models.CharField(
                        choices=[
                            ("B", "Bolsa Família"),
                            ("A", "Aposentadoria"),
                            ("S", "Seguro Desemprego"),
                            ("O", "Outro"),
                            ("U", "Bolsa Universidade"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "pensamentoSuicida",
                    models.CharField(
                        choices=[("S", "Sim"), ("N", "Não")], max_length=1
                    ),
                ),
                (
                    "tentativaSuicidio",
                    models.CharField(
                        choices=[("S", "Sim"), ("N", "Não")], max_length=1
                    ),
                ),
                (
                    "nivelEscolaridade",
                    models.CharField(
                        choices=[
                            ("A", "Analfabeto"),
                            ("F", "Fundamental"),
                            ("M", "Médio"),
                            ("S", "Superior"),
                            ("P", "Pós-Graduação"),
                        ],
                        max_length=2,
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "LGBT - Exame Endocrinologia",
            },
        ),
    ]
