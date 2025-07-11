# Generated by Django 5.2.2 on 2025-06-07 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_blog_image_alter_blog_section_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='section',
            field=models.CharField(choices=[('Recent', 'Recent'), ('Trending', 'Trending'), ('Publish', 'Publish')], default='Recent', max_length=200),
        ),
    ]
