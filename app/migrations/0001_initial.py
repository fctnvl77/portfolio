# Generated by Django 4.1.7 on 2023-03-30 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(blank=True, null=True, upload_to='blog_rasmlar')),
                ('mavzu', models.CharField(max_length=100)),
                ('batafsil', models.TextField(max_length=100)),
                ('blog_raqam', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Bloglar',
            },
        ),
        migrations.CreateModel(
            name='Men',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=100)),
                ('rasm', models.ImageField(blank=True, null=True, upload_to='rasmlarim')),
                ('men_xaqimda', models.TextField()),
                ('yil', models.DateField()),
                ('manzil', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=30)),
                ('tajriba_yil', models.IntegerField()),
                ('loyihalar_soni', models.IntegerField()),
                ('yutuqlar_soni', models.IntegerField()),
                ('ish_vaqt', models.FloatField()),
            ],
            options={
                'verbose_name': 'Men_haqimda',
                'verbose_name_plural': 'Men haqimda',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(blank=True, null=True, upload_to='loyiha_rasmlar')),
                ('nomi', models.CharField(max_length=100)),
                ('malumot', models.TextField(max_length=100)),
                ('link', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfoliolar',
            },
        ),
        migrations.CreateModel(
            name='Rezyume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rezyume', models.FileField(upload_to='rezyumelarim')),
            ],
        ),
    ]
