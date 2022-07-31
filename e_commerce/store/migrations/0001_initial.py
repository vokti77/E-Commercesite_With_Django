# Generated by Django 4.0.4 on 2022-04-16 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='category')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='store.category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('previous_des', models.CharField(max_length=100, verbose_name='Short Description')),
                ('description', models.CharField(max_length=250, verbose_name='Description')),
                ('image', models.ImageField(upload_to='product')),
                ('price', models.FloatField()),
                ('old_price', models.FloatField(blank=True, default=0.0, null=True)),
                ('is_stock', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='store.category')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
