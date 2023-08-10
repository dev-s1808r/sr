from django.db import models
from django.utils.translation import gettext_lazy as _


class Tags(models.Model):
    tag = models.CharField(_("tags"), max_length=128)


class Post(models.Model):

    class Language(models.TextChoices):
        MARATHI = 'MR', "Marathi"
        ENGLISH = 'EN', "English"

    title = models.CharField(_("title"), max_length=512)
    abstract = models.CharField(_("abstract"), max_length=1024)
    body = models.TextField(_("content"))
    slug = models.SlugField(_("slug"))
    published = models.DateTimeField(_("created"), auto_now_add=True)
    updated = models.DateTimeField(_("published"), auto_now=True)
    language = models.CharField(
        _("language"), max_length=2, choices=Language.choices, default=Language.MARATHI)
    tags = models.ManyToManyField(Tags, related_name='tags')

    class Meta:
        ordering = ["-published"]
