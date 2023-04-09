# Generated by Django 4.1 on 2023-04-09 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_product_rename_product_opinion__product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opinion',
            name='_product',
        ),
        migrations.AddField(
            model_name='opinion',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.product'),
        ),
        migrations.AlterField(
            model_name='opinion',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
