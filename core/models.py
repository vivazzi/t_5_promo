from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField


class SliderItem(models.Model):
    title = models.CharField(_('Title'), max_length=255, help_text=_('Display in admin only'))
    image = FilerImageField(verbose_name=_('Image'), null=True, blank=True, related_name='image_slider_item',
                            on_delete=models.SET_NULL)

    order = models.PositiveSmallIntegerField(_('Order'), db_index=True, default=0, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('order',)
        verbose_name = _('Slider item')
        verbose_name_plural = _('Slider items')
