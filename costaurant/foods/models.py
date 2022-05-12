from django.db import models

# Models의 model을 상속받아 사용해야함


class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    img_path = models.CharField(max_length=255)

    def __str__(self):
        return self.name
