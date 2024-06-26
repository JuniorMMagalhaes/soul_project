# Generated by Django 4.2.11 on 2024-05-04 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_customer', '0003_alter_adress_addr_complement_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='companyAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('company_fantasy_name', models.CharField(max_length=255)),
                ('company_document', models.CharField(max_length=255)),
                ('company_phone', models.CharField(max_length=255)),
                ('company_email', models.EmailField(max_length=255)),
                ('company_registration', models.DateTimeField(auto_now_add=True)),
                ('address', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_customer.adress')),
            ],
        ),
    ]
