from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, default='')
    surname = models.CharField(max_length=20, default='')
    position = models.CharField(max_length=20, default='')
    photo = models.ImageField(default='default.jpg', upload_to='upload_pics')

    class Meta:
        verbose_name = 'Profile Info'
        verbose_name_plural = 'Profiles'
        ordering = ('first_name', 'surname')

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        photo = Image.open(self.photo.path)
        if photo.height > 100 or photo.width > 100:
            new_size = (100, 100)
            photo.thumbnail(new_size)
            photo.save(self.photo.path)
