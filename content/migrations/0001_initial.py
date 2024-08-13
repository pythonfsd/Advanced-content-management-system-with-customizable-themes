# Generated by Django 5.0.6 on 2024-06-18 01:08

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('text_content', models.TextField(blank=True, null=True)),
                ('image_content', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('video_content', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('pdf_content', models.FileField(blank=True, null=True, upload_to='pdfs/')),
                ('word_content', models.FileField(blank=True, null=True, upload_to='words/')),
                ('audio_content', models.FileField(blank=True, null=True, upload_to='audios/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]