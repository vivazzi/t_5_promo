# Generated by Django 4.1.5 on 2023-01-25 03:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Display in admin only', max_length=255, verbose_name='Title')),
                ('order', models.PositiveSmallIntegerField(db_index=True, default=0, verbose_name='Order')),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_slider_item', to=settings.FILER_IMAGE_MODEL, verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Slider item',
                'verbose_name_plural': 'Slider items',
                'ordering': ('order',),
            },
        ),
    ]
