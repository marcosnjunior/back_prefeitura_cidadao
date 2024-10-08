

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("infraestrutura", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expansao_iluminacao",
            name="numeroRecidencia",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="galeriabocalobo",
            name="numeroRecidencia",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="problema_iluminacao",
            name="numeroRecidencia",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="tapa_buraco",
            name="numeroRecidencia",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="terraplanagem",
            name="numeroRecidencia",
            field=models.IntegerField(),
        ),
    ]
