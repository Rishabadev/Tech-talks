# Generated by Django 5.1.5 on 2025-04-18 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techtalks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ReviewComment',
        ),
    ]
