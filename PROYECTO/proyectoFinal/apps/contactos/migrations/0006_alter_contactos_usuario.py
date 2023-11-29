# Generated by Django 4.2.3 on 2023-07-26 01:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contactos', '0005_rename_user_contactos_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactos',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]