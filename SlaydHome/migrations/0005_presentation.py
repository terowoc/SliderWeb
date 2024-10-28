# Generated by Django 5.1.2 on 2024-10-27 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SlaydHome', '0004_webdesignmodel3_webdesignmodel4_webdesignmodel5_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('ppt_file', models.FileField(upload_to='presentations/')),
                ('html_file', models.FileField(blank=True, null=True, upload_to='html_presentations/')),
            ],
        ),
    ]
