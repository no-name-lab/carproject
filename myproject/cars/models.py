from django.db import models

class Marka(models.Model):
    marka_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.marka_name

class CarModel(models.Model):
    car_model = models.CharField(max_length=100,unique=True)
    car_marka = models.ForeignKey(Marka, on_delete=models.CASCADE)

    def __str__(self):
        return self.car_model

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    description = models.TextField()
    year = models.DateField
    price = models.PositiveIntegerField(default=1000)
    color = models.CharField(max_length=50)
    volume = models.DecimalField(max_digits=3, decimal_places=1)
    video = models.FileField(upload_to='car_videos/', null=True, blank=True)

    def __str__(self):
        return self.car_name

class CarPhoto(models.Model):
    car_image = models.ImageField(upload_to='car_imgs/')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)


