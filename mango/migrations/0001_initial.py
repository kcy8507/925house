# Generated by Django 4.1.3 on 2025-03-04 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='이름')),
                ('thumb', models.ImageField(upload_to='thumb/%Y/%m/%d', verbose_name='썸네일이미지')),
                ('image', models.ImageField(upload_to='image/%Y/%m/%d', verbose_name='이미지')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
            ],
            options={
                'verbose_name': '포토폴리오',
                'verbose_name_plural': '포토폴리오',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business', models.CharField(blank=True, max_length=50, null=True, verbose_name='회사명')),
                ('industry', models.CharField(blank=True, max_length=50, null=True, verbose_name='업종')),
                ('manager_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='담당자명')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='연락처')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='이메일')),
                ('budget', models.CharField(max_length=10, verbose_name='예산')),
                ('needs', models.TextField(blank=True, null=True, verbose_name='문의사항')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
            ],
            options={
                'verbose_name': '의뢰목록',
                'verbose_name_plural': '의뢰목록',
            },
        ),
    ]
