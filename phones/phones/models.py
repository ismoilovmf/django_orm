from django.db import models

#id;name;image;price;release_date;lte_exists
class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=25)
    image = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    release_date = models.CharField(max_length=15)
    lte_exists = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
