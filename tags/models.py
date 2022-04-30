from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from store.models import Product


class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # what tag is applied to what object (Generic)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # Type of the Object also the we need the Id of the object
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # watch out if the id is not an integer
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
