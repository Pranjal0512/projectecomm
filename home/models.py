from django.db import models
from django.contrib.auth.models import User



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


class Slider(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    url = models.URLField(max_length=500,blank = True)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.name

class Ad(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    rank = models.IntegerField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
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

class Wishlist(models.Model):
    username = models.CharField(max_length=300)
    name = models.CharField(max_length=200)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    username = models.CharField(max_length=300)
    slug = models.CharField(max_length=300)
    quantity = models.IntegerField()
    total = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    checkout = models.BooleanField(default = False)
    items = models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
        return self.username

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
class BlogComment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.post.title

class Checkout(models.Model):
    username = models.CharField(max_length=300)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return self.username

class Gallery(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    description = models.TextField()

    def __str__(self):
        return self.name





