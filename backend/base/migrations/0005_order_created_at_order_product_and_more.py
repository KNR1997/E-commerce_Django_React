# Generated by Django 5.0.4 on 2024-04-06 15:28

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_product_quantity'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='base.product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders_updated', to=settings.AUTH_USER_MODEL),
        ),
    ]
