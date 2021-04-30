from django.db import models
from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone

# Create your models here.


class Tweet(models.Model):
    # By default, Django gives each model the below field.
    # id = models.AutoField(primary_key=True)
    name = models.CharField("Name", max_length=30)
    body = models.TextField("Caption", max_length=200)
    image = CloudinaryField(
        "Image",
        overwrite=True,
        blank=True,
        resource_type="image",
        transformation=[
            {"auto": "responsive", "width": 1024,
                "height": 768, "crop": "pad", 'radius': 20, }
        ],
        format="jpg",
    )
    # {"auto": "responsive", "width": 720, "crop": "pad"}

    like_count = models.IntegerField(
        "Total counts of Like", default=0, blank=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.name
