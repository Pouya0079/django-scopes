from django.contrib.auth.models import AbstractUser

from .base import BaseModel, models


class Staff(BaseModel, AbstractUser):

    def staff_pic_dir(self, filename):
        return f'media/staff/staff_{self._id}/{filename}'

    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    store = models.ForeignKey('Store', on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=staff_pic_dir)
