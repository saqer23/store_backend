# Generated by Django 3.2.5 on 2021-09-09 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_coment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coment',
            name='prod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.products'),
        ),
    ]