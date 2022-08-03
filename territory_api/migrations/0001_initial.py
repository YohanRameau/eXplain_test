# Generated by Django 4.1 on 2022-08-03 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Territory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('kind', models.CharField(choices=[('FRCOMM', 'Frcomm'), ('FREPCI', 'Frepci'), ('FRDEPA', 'Frdepa'), ('FRCANT', 'Frcant')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_current', models.BooleanField(null=True)),
                ('population', models.IntegerField(default=0)),
                ('official_website_url', models.CharField(max_length=50, null=True)),
                ('articles_count', models.IntegerField(default=0)),
                ('admin_docs_count', models.IntegerField(default=0)),
                ('impacters_count', models.IntegerField(default=0)),
                ('websites_count', models.IntegerField(default=0)),
                ('sources_count', models.IntegerField(default=0)),
            ],
        ),
    ]
