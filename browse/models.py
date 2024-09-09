from django.db import models

# Create your models here.
class Book(models.Model):
    choice=[
        ('sold','sold'),('available','available'),('for rent','for rent')]
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    state = models.CharField(max_length=50,choices=choice)
    image = models.ImageField(upload_to='photos/%y/%m/%d',max_length=1000)
    def __str__(self) :
        return self.name

