# Generated by Django 5.1.5 on 2025-04-02 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='product_images/'),
            preserve_default=False,
        ),
    ]
