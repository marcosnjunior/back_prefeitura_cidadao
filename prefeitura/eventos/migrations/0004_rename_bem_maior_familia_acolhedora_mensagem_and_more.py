# Generated by Django 5.0 on 2024-08-21 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "eventos",
            "0003_alter_conselho_tutelar_options_alter_cultura_options_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="familia_acolhedora",
            old_name="bem_maior",
            new_name="mensagem",
        ),
        migrations.AlterField(
            model_name="familia_acolhedora",
            name="bairro",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora",
            name="celular",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora",
            name="cep",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora",
            name="cidade",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora",
            name="complemento",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora",
            name="cpf",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora",
            name="data_nascimneto",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora",
            name="email",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora",
            name="endereco",
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora",
            name="genero_acolhimento",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora",
            name="idade",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora",
            name="nome",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora",
            name="numero_residencia",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora",
            name="ponto_referencia",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora",
            name="preferencia_perfil",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora",
            name="renda",
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora",
            name="renda_aproximada",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora",
            name="residente",
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora",
            name="rg",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora",
            name="sabendo_servico",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora",
            name="telefone",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="familia_acolhedora",
            name="uf",
            field=models.CharField(max_length=10),
        ),
    ]
