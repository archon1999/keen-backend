# Generated by Django 4.2.9 on 2024-09-21 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='problems.category'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ProblemCategory',
        ),
    ]
