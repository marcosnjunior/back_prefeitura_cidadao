# Generated by Django 5.0 on 2024-08-23 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "eventos",
            "0010_conselho_tutelar_cristo_conselho_tutelar_mangabeira_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Familia_acolhedora_forms",
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
                ("nome", models.CharField(default="null", max_length=100)),
                ("idade", models.IntegerField(default=0)),
                ("data_nascimento", models.IntegerField(default=0)),
                ("cpf", models.IntegerField(default=0)),
                ("rg", models.IntegerField(default=0)),
                ("endereco", models.CharField(default="null", max_length=300)),
                ("numero_residencia", models.IntegerField(default=0)),
                ("cep", models.IntegerField(default=0)),
                ("ponto_referencia", models.CharField(default="null", max_length=200)),
                ("bairro", models.CharField(default="null", max_length=150)),
                ("cidade", models.CharField(default="null", max_length=150)),
                ("uf", models.CharField(default="null", max_length=10)),
                ("complemento", models.CharField(default="null", max_length=200)),
                ("telefone", models.IntegerField(default=0)),
                ("celular", models.IntegerField(default=0)),
                ("email", models.CharField(default="null", max_length=150)),
                ("sabendo_servico", models.CharField(default="null", max_length=150)),
                ("preferencia_perfil", models.TextField(default="null")),
                ("genero_acolhimento", models.CharField(default="null", max_length=20)),
                ("renda", models.CharField(default="null", max_length=5)),
                ("renda_aproximada", models.CharField(default="null", max_length=100)),
                ("residente", models.CharField(default="null", max_length=5)),
                ("mensagem", models.TextField(default="null")),
            ],
            options={
                "verbose_name": "Família Acolhedora",
            },
        ),
        migrations.CreateModel(
            name="Funjope_Apoio_a_eventos_artisticos",
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
                ("descricao", models.TextField()),
            ],
            options={
                "verbose_name": "FUNJOPE - Apoio a Eventos Artisticos e Culturais",
            },
        ),
        migrations.CreateModel(
            name="Funjope_atestado_da_condicao_de_artista_local",
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
                ("descricao", models.TextField()),
            ],
            options={
                "verbose_name": "FUNJOPE - Atestado da Condição de Artista Local",
            },
        ),
        migrations.CreateModel(
            name="Funjope_cadastramento_de_artistas_e_outros",
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
                ("descricao", models.TextField()),
            ],
            options={
                "verbose_name": "FUNJOPE - Cadastramento de Artistas e Outros",
            },
        ),
        migrations.CreateModel(
            name="Funjope_concertos_de_orquestra_sinfonica",
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
                ("descricao", models.TextField()),
            ],
            options={
                "verbose_name": "FUNJOPE - Concertos de Orquestra Sinfônica Municipal de João Pessoa (OSMJP)",
            },
        ),
        migrations.CreateModel(
            name="Funjope_edital_de_ocupacao_do_casa_da_polvora",
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
                ("descricao", models.TextField()),
            ],
            options={
                "verbose_name": "FUNJOPE - Edital de Ocupação do Casa da Pólvora",
            },
        ),
        migrations.CreateModel(
            name="Funjope_edital_de_ocupacao_do_casarao_34",
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
                ("descricao", models.TextField()),
            ],
            options={
                "verbose_name": "FUNJOPE - Edital de Ocupação do Casarão 34",
            },
        ),
        migrations.CreateModel(
            name="Funjope_edital_de_ocupacao_do_hotel_globo",
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
                ("descricao", models.TextField()),
            ],
            options={
                "verbose_name": "FUNJOPE - Edital de Ocupação do Hotel Globo",
            },
        ),
        migrations.CreateModel(
            name="Funjope_exposicao_de_artes_visuais",
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
                ("descricao", models.TextField()),
            ],
            options={
                "verbose_name": "FUNJOPE - Exposição de Artes Visuais, Oficinas Culturais, Seminários e Palestras",
            },
        ),
        migrations.CreateModel(
            name="Funjope_instalacao_de_obras_de_arte",
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
                ("descricao", models.TextField()),
            ],
            options={
                "verbose_name": "FUNJOPE - Instalação de Obras de Arte",
            },
        ),
        migrations.CreateModel(
            name="Funjope_jp_cultura",
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
                ("descricao", models.TextField()),
            ],
            options={
                "verbose_name": "FUNJOPE - JP Cultura",
            },
        ),
        migrations.CreateModel(
            name="Funjope_jp_film_commission",
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
                ("descricao", models.TextField()),
            ],
            options={
                "verbose_name": "FUNJOPE - JP Film Commission",
            },
        ),
        migrations.CreateModel(
            name="Funjope_lei_dos_edificios",
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
                ("descricao", models.TextField()),
            ],
            options={
                "verbose_name": "FUNJOPE - Lei dos Edifícios",
            },
        ),
        migrations.CreateModel(
            name="Funjope_prestacao_de_contas",
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
                ("descricao", models.TextField()),
            ],
            options={
                "verbose_name": 'FUNJOPE - Prestação de Contas"',
            },
        ),
        migrations.CreateModel(
            name="Funjope_projeto_acao_social_pela_musica",
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
                ("descricao", models.TextField()),
            ],
            options={
                "verbose_name": "FUNJOPE - Projeto Ação Social pela Música",
            },
        ),
        migrations.CreateModel(
            name="Funjope_solicitacao_de_pagamento",
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
                ("descricao", models.TextField()),
            ],
            options={
                "verbose_name": "FUNJOPE - Solicitação de Pagamento",
            },
        ),
        migrations.RemoveField(
            model_name="conselho_tutelar",
            name="nome",
        ),
        migrations.RemoveField(
            model_name="cultura",
            name="nome",
        ),
        migrations.RemoveField(
            model_name="familia_acolhedora",
            name="bairro",
        ),
        migrations.RemoveField(
            model_name="familia_acolhedora",
            name="celular",
        ),
        migrations.RemoveField(
            model_name="familia_acolhedora",
            name="cep",
        ),
        migrations.RemoveField(
            model_name="familia_acolhedora",
            name="cidade",
        ),
        migrations.RemoveField(
            model_name="familia_acolhedora",
            name="complemento",
        ),
        migrations.RemoveField(
            model_name="familia_acolhedora",
            name="cpf",
        ),
        migrations.RemoveField(
            model_name="familia_acolhedora",
            name="data_nascimneto",
        ),
        migrations.RemoveField(
            model_name="familia_acolhedora",
            name="email",
        ),
        migrations.RemoveField(
            model_name="familia_acolhedora",
            name="endereco",
        ),
        migrations.RemoveField(
            model_name="familia_acolhedora",
            name="genero_acolhimento",
        ),
        migrations.RemoveField(
            model_name="familia_acolhedora",
            name="idade",
        ),
        migrations.RemoveField(
            model_name="familia_acolhedora",
            name="mensagem",
        ),
        migrations.RemoveField(
            model_name="familia_acolhedora",
            name="nome",
        ),
        migrations.RemoveField(
            model_name="familia_acolhedora",
            name="numero_residencia",
        ),
        migrations.RemoveField(
            model_name="familia_acolhedora",
            name="ponto_referencia",
        ),
        migrations.RemoveField(
            model_name="familia_acolhedora",
            name="preferencia_perfil",
        ),
        migrations.RemoveField(
            model_name="familia_acolhedora",
            name="renda",
        ),
        migrations.RemoveField(
            model_name="familia_acolhedora",
            name="renda_aproximada",
        ),
        migrations.RemoveField(
            model_name="familia_acolhedora",
            name="residente",
        ),
        migrations.RemoveField(
            model_name="familia_acolhedora",
            name="rg",
        ),
        migrations.RemoveField(
            model_name="familia_acolhedora",
            name="sabendo_servico",
        ),
        migrations.RemoveField(
            model_name="familia_acolhedora",
            name="telefone",
        ),
        migrations.RemoveField(
            model_name="familia_acolhedora",
            name="uf",
        ),
    ]
