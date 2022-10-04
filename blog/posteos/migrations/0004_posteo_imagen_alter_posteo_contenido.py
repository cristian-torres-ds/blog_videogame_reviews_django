# Generated by Django 4.1 on 2022-10-03 20:08

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posteos', '0003_posteo_puntaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='posteo',
            name='imagen',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='posteo',
            name='contenido',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
