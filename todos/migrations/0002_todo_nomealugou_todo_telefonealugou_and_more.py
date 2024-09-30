# Generated by Django 5.1.1 on 2024-09-29 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="nomeAlugou",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="todo",
            name="telefoneAlugou",
            field=models.IntegerField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name="todo",
            name="dataAlugou",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="todo",
            name="dataDevol",
            field=models.DateTimeField(null=True),
        ),
    ]
