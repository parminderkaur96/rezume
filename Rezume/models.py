from django.db import models

# Create your models here.
class Testomonial(models.Model):
    name =models.CharField(max_length=100)

    title=models.CharField(max_length=100)

    image = models.ImageField(upload_to='image/', null=True, blank=True)


class Service(models.Model):
    title =models.CharField(max_length=100)
    desc=models.TextField()
    image = models.ImageField(upload_to='image/', null=True, blank=True)
class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
class Resume(models.Model):
    start_at = models.DateTimeField(blank=False)
    end_at = models.DateTimeField(blank=True)
    title = models.CharField(max_length=100)
    desc = models.TextField()

    def _str_(self):
        return self.name
class Education(models.Model):
    start_at = models.DateTimeField(blank=False)
    end_at = models.DateTimeField(blank=True)
    title = models.CharField(max_length=100)
    desc = models.TextField()

    def _str_(self):
        return self.name
class Contact(models.Model):
        name = models.CharField(max_length=200)
        email = models.EmailField(max_length=200)
        message = models.TextField()

        def _str_(self):
            return self.name

class Potfolio(models.Model):
    image=models.ImageField(upload_to='image/', null=True, blank=True)
    title=models.CharField(max_length=100)
    name=models.CharField(max_length=100)

