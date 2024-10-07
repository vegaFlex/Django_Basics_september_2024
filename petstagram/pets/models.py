from django.db import models
from django.template.defaultfilters import slugify

class Pet(models.Model):
    name = models.CharField(max_length=30)
    personal_photo = models.URLField()
    date_of_birth = models.DateField(null=True, blank=True)
    slug = models.SlugField(null = False, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name