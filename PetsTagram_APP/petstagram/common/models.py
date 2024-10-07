from django.db import models

from petstagram.photos.models import Photo


class Comment(models.Model):
    text = models.TextField(max_length=300)
    to_photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE)
    date_of_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Like(models.Model):
    to_photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE)

