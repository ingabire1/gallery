from django.db import models
import datetime as dt

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()

    class Meta:
        ordering = ['first_name']

# class tags(models.Model):
#     name = models.CharField(max_length =30)

#     def __str__(self):
#         return self.name
class Category(models.Model):
    title = models.CharField(max_length =60)
   
class location(models.Model):
    title = models.CharField(max_length =60)
   

class Image(models.Model):
    title = models.CharField(max_length =60)
    description = models.TextField()
    editor = models.ForeignKey(Editor)
    location = models.ForeignKey(location,blank=True)
    category = models.ForeignKey(Category,blank=True)
    # tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    image_image = models.ImageField(upload_to = 'images/',blank=True)

    @classmethod
    def todays_images(cls,date):
        today = dt.date.today()
        images = cls.objects.filter(pub_date__date = today)
        return images

    @classmethod
    def search_by_title(cls,search_term):
        images = cls.objects.filter(title__icontains=search_term)
        return images


