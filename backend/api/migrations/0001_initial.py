# Generated by Django 5.0.6 on 2024-07-12 17:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('code', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('duration', models.FloatField()),
                ('output', models.TextField()),
                ('errors', models.TextField()),
                ('related_experiment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='api.experiment')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.AddField(
            model_name='experiment',
            name='related_results',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='experiment', to='api.results'),
        ),
    ]
