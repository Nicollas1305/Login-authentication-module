# Generated by Django 4.2.7 on 2024-02-23 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("nome", models.CharField(max_length=150)),
                (
                    "foto_perfil",
                    models.ImageField(blank=True, null=True, upload_to="profile_pics/"),
                ),
                ("data_nascimento", models.DateField(blank=True, null=True)),
                ("telefone", models.CharField(blank=True, max_length=20, null=True)),
                ("endereco", models.CharField(blank=True, max_length=255, null=True)),
                ("token_auth", models.CharField(blank=True, max_length=255, null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
