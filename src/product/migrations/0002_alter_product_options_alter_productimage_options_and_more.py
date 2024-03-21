# Generated by Django 4.2.11 on 2024-03-21 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='productvariant',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='productvariantprice',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='variant',
            options={'ordering': ('id',)},
        ),
        migrations.AlterField(
            model_name='productvariantprice',
            name='product_variant_one',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_variant_one', to='product.productvariant'),
        ),
        migrations.AlterField(
            model_name='productvariantprice',
            name='product_variant_three',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_variant_three', to='product.productvariant'),
        ),
        migrations.AlterField(
            model_name='productvariantprice',
            name='product_variant_two',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_variant_two', to='product.productvariant'),
        ),
    ]
