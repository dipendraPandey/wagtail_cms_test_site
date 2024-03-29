from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


# Create your models here.
@register_setting
class SocialMediaSettings(BaseSetting):
    """social medial setting for our custom website """
    facebook = models.URLField(blank=True, null=True, help_text='Facebook URL')
    twitter = models.URLField(blank=True, null=True, help_text='Twitter URL')
    youtube = models.URLField(blank=True, null=True, help_text='Youtube Channel URL')
    instagram = models.URLField(blank=True, null=True, help_text='Instagram URL')

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("youtube"),
            FieldPanel("instagram"),
        ])

    ]
