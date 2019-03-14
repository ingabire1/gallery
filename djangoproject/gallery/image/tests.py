from django.test import TestCase
from .models import Editor,Image
import datetime as dt

# Create your tests here.

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')

    # Testing  instance

    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))

class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_image= Image(title = 'Test Image',post = 'This is a random test Post',editor = self.james)
        self.new_image.save()

        self.new_image.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        # tags.objects.all().delete()
        Image.objects.all().delete()

    def test_get_images_today(self):
        today_images = Images.todays_images()
        self.assertTrue(len(today_images)>0)

        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        images_by_date = Images.days_images(date)
        self.assertTrue(len(images_by_date) == 0)

