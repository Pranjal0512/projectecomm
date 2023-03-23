from django.db import models

class Service(models.Model):
    title= models.CharField(max_length=300)
    logo = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.title


class  Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name
class Information(models.Model):
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=300)
    time = models. CharField(max_length=20)


    def __str__(self):
        return self.address1

class Ad(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name