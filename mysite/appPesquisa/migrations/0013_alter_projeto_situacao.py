# Generated by Django 4.2.1 on 2023-07-09 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPesquisa', '0012_merge_20230709_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='situacao',
            field=models.CharField(choices=[('em andamento', 'Em andamento'), ('encerrado', 'Encerrado'), ('prorrogado', 'Prorrogado')], max_length=100),
        ),
    ]
