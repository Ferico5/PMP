# Generated by Django 4.2.16 on 2024-10-23 04:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pos_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableResto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('capacity', models.IntegerField(default=0)),
                ('table_status', models.CharField(choices=[('Kosong', 'Kosong'), ('Terisi', 'Terisi')], default='Kosong', max_length=15)),
                ('status', models.CharField(choices=[('Aktif', 'Aktif'), ('Tidak Aktif', 'Tidak Aktif')], default='Aktif', max_length=15)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('user_create', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_create_table_resto', to=settings.AUTH_USER_MODEL)),
                ('user_update', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_update_table_resto', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
