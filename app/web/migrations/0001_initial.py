# Generated by Django 2.2.16 on 2020-12-24 10:04

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, default='', null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('thumbnail', models.ImageField(upload_to='media/Post/thumbnail/')),
                ('status', models.CharField(choices=[('a', 'active'), ('d', 'deactive'), ('u', 'unknown')], max_length=1)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-created_at'],
            },
        ),
    ]
