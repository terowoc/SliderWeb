# Generated by Django 5.1.2 on 2024-10-20 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SlaydHome', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebDesignModel1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('slide_file', models.FileField(upload_to='slides')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'slayd1_article_model',
            },
        ),
        migrations.DeleteModel(
            name='Web_designModel',
        ),
    ]
