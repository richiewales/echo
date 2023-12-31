# Generated by Django 4.2.4 on 2023-09-04 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=60)),
                ('author_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.CharField(max_length=38, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('post_text', models.CharField(max_length=300)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.user')),
            ],
        ),
    ]
