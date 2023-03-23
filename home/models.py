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

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=500,unique=True)
    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    slug = models.CharField(max_length=500,unique=True)

    def __str__(self):
        return self.name

STATUS = (('Active','Active'),('Inactive','Inactive'))
LABELS = (('new','new'),('featured','featured'),('all','all'),('offer','offer'),('','default'))
class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    discounted_price = models.IntegerField()
    image = models.ImageField(upload_to='media')
    description = models.TextField()
    specification = models.TextField()
    slug = models.CharField(max_length=500,unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    labels = models.CharField(choices=LABELS,max_length=50)
    status = models.CharField(choices=STATUS, max_length=50)
    def __str__(self):
        return self.name
