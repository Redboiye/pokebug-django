# Generated by Django 5.1.1 on 2024-09-23 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0003_alter_pokemon_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='video',
            field=models.TextField(null=True),
        ),
    ]
