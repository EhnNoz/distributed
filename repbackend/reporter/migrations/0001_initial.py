# Generated by Django 4.2.21 on 2025-06-01 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('channel_id', models.CharField(max_length=100, unique=True)),
                ('topic', models.CharField(max_length=100)),
                ('sub_topic', models.CharField(max_length=100)),
                ('audience', models.TextField()),
                ('created_at', models.DateField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to='channel_pictures/')),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='platform_logos/')),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_text', models.TextField()),
                ('hashtags', models.TextField()),
                ('views', models.PositiveIntegerField()),
                ('collected_at', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.author')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='reporter.channel')),
            ],
        ),
        migrations.CreateModel(
            name='ChannelMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_count', models.PositiveIntegerField()),
                ('collected_at', models.DateField()),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='reporter.channel')),
            ],
        ),
        migrations.AddField(
            model_name='channel',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.platform'),
        ),
        migrations.AddField(
            model_name='channel',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.province'),
        ),
    ]
