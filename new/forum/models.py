from django.db import models

# Create your models here.

from taggit.managers import TaggableManager
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image

from multiselectfield import MultiSelectField
from datetime import datetime

def upload_location(instance,filename):
    print ("%s/%s"%(instance.id,filename))
    return "%s/%s"%(instance.id,filename)

class entire_house(models.Model):
    user_name = models.CharField(max_length=120, null=True)
    user = models.CharField(max_length=120, null=True)
    email = models.EmailField(max_length=120, null=True)
    City = models.CharField(max_length=100, blank=False, null=True)
    Area = models.CharField(max_length=100, blank=False, null=True)
    Address = models.CharField(max_length=200, blank=False, null=True)
    house_type=(('flat','flat'),('seperate house','seperate house'))
    house=models.CharField(max_length=20,choices=house_type,default='flat')
    rent = models.IntegerField(default=0)
    securitydeposit = models.IntegerField(default=0)
    Numbers = [(i, i) for i in range(11)]
    Area_sqft = models.IntegerField(default=0)
    bed_rooms = models.IntegerField(choices=Numbers, default=0)
    bathrooms = models.IntegerField(choices=Numbers, default=0)
    kitchen = models.IntegerField(choices=Numbers, default=0)
    hall = models.IntegerField(choices=Numbers, default=0)
    gender_choices = (('male', 'male'), ('female', 'female'), ('family', 'family'), ('any', 'any'))
    gender = models.CharField(max_length=20, choices=gender_choices, default="any")
    Furniture_choices = (('full', 'full furnished'), ('semi', 'semi furnished'), ('no', 'no furnished'))
    Furniture = models.CharField(max_length=20, choices=Furniture_choices, default='full')
    available_choices = (('yes', 'Yes'), ('no', 'No'))
    Available = models.CharField(max_length=10, choices=available_choices, default='no')
    essential_amenities = (('parking', 'Car parking'),
                           ('security', 'Security services'),
                           ('water', 'Water supply'),
                           ('elevator', 'Elevators'),
                           ('power', 'Power backup'),
                           ('maintenance', '24-hour maintenance'))
    essentialamenities = MultiSelectField(choices=essential_amenities, default='parking')
    optional_amenities = (('play', 'Play area'),
                          ('gym', 'Gym'),
                          ('salon', 'Spa and salon'),
                          ('Concierge', 'Concierge services'),
                          ('hospital', 'Hospitals'),
                          ('restaurant', 'Restaurants'),
                          ('temples', 'Temple and religious activity place'),
                          ('wifi', 'Wi-Fi connectivity'))
    optionalamenities = MultiSelectField(choices=optional_amenities, default='play')
    description = models.TextField(blank=False, null=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    image1 = models.ImageField(upload_to=upload_location, verbose_name='Image(optional)', blank=True)
    image2 = models.ImageField(upload_to=upload_location, verbose_name='Image(optional)', blank=True)
    image3 = models.ImageField(upload_to=upload_location, verbose_name='Image(optional)', blank=True)
    image4 = models.ImageField(upload_to=upload_location, verbose_name='Image(optional)', blank=True)
    image5 = models.ImageField(upload_to=upload_location, verbose_name='Image(optional)', blank=True)
    image6 = models.ImageField(upload_to=upload_location, verbose_name='Image(optional)', blank=True)

    def get_absolute_url(self):
        return reverse("entirehouse-detail", kwargs={"my_id": self.id})
        return f"/question_list/{self.id}/"

    class Meta:
        ordering = ["-updated", "-timestamp"]
class entire_house_Images(models.Model):
    sharedroom = models.ForeignKey(entire_house, default=None ,on_delete=models.CASCADE,)
    image = models.ImageField(upload_to=upload_location,
                              verbose_name='Image(optional)',blank=True
                              )

class private_room(models.Model):
    user_name = models.CharField(max_length=120, null=True)
    user = models.CharField(max_length=120, null=True)
    email = models.EmailField(max_length=120, null=True)
    City = models.CharField(max_length=100, blank=False, null=True)
    Area = models.CharField(max_length=100, blank=False, null=True)
    Address = models.CharField(max_length=200, blank=False, null=True)
    rent = models.IntegerField(default=0)
    securitydeposit = models.IntegerField(default=0)
    Numbers = [(i, i) for i in range(11)]
    Area_sqft = models.IntegerField(default=0)
    bed_rooms = models.IntegerField(choices=Numbers, default=0)
    bathrooms = models.IntegerField(choices=Numbers, default=0)
    kitchen = models.IntegerField(choices=Numbers, default=0)
    hall = models.IntegerField(choices=Numbers, default=0)
    rooms_available = models.IntegerField(default=0)
    gender_choices = (('male', 'male'), ('female', 'female'), ('family', 'family'), ('any', 'any'))
    gender = models.CharField(max_length=20, choices=gender_choices, default="any")
    Furniture_choices = (('full', 'full furnished'), ('semi', 'semi furnished'), ('no', 'no furnished'))
    Furniture = models.CharField(max_length=20, choices=Furniture_choices, default='full')
    available_choices = (('yes', 'Yes'), ('no', 'No'))
    Available = models.CharField(max_length=10, choices=available_choices, default='no')
    essential_amenities = (('parking', 'Car parking'),
                           ('security', 'Security services'),
                           ('water', 'Water supply'),
                           ('elevator', 'Elevators'),
                           ('power', 'Power backup'),
                           ('maintenance', '24-hour maintenance'))
    essentialamenities = MultiSelectField(choices=essential_amenities, default='parking')
    optional_amenities = (('play', 'Play area'),
                          ('gym', 'Gym'),
                          ('salon', 'Spa and salon'),
                          ('Concierge', 'Concierge services'),
                          ('hospital', 'Hospitals'),
                          ('restaurant', 'Restaurants'),
                          ('temples', 'Temple and religious activity place'),
                          ('wifi', 'Wi-Fi connectivity'))
    optionalamenities = MultiSelectField(choices=optional_amenities, default='play')
    description = models.TextField(blank=False, null=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    image1 = models.ImageField(upload_to=upload_location, verbose_name='Image(optional)', blank=True)
    image2 = models.ImageField(upload_to=upload_location, verbose_name='Image(optional)', blank=True)
    image3 = models.ImageField(upload_to=upload_location, verbose_name='Image(optional)', blank=True)
    image4 = models.ImageField(upload_to=upload_location, verbose_name='Image(optional)', blank=True)
    image5 = models.ImageField(upload_to=upload_location, verbose_name='Image(optional)', blank=True)
    image6 = models.ImageField(upload_to=upload_location, verbose_name='Image(optional)', blank=True)

    def get_absolute_url(self):
        return reverse("privateroom-detail", kwargs={"my_id": self.id})
        return f"/question_list/{self.id}/"

    class Meta:
        ordering = ["-updated", "-timestamp"]

class private_room_Images(models.Model):
    sharedroom = models.ForeignKey(private_room, default=None ,on_delete=models.CASCADE,)
    image = models.ImageField(upload_to=upload_location,
                              verbose_name='Image(optional)',blank=True
                              )

class shared_room(models.Model):
    user_name = models.CharField(max_length=120, null=True)
    user=models.CharField(max_length=120,null=True)
    email=models.EmailField(max_length=120,null=True)
    City=models.CharField(max_length=100,blank=False,null=True)
    Area=models.CharField(max_length=100,blank=False,null=True)
    Address=models.CharField(max_length=200,blank=False,null=True)
    rent=models.IntegerField(default=0)
    securitydeposit=models.IntegerField(default=0)
    Numbers=[(i,i) for i in range(11)]
    Area_sqft=models.IntegerField(default=0)
    bed_rooms=models.IntegerField(choices=Numbers,default=0)
    bathrooms=models.IntegerField(choices=Numbers,default=0)
    kitchen = models.IntegerField(choices=Numbers, default=0)
    hall = models.IntegerField(choices=Numbers, default=0)
    beds_available=models.IntegerField(default=0)
    gender_choices=(('male','male'),('female','female'),('family','family'),('any','any'))
    gender=models.CharField(max_length=20,choices=gender_choices,default="any")
    Furniture_choices=(('full','full furnished'),('semi','semi furnished'),('no','no furnished'))
    Furniture=models.CharField(max_length=20,choices=Furniture_choices,default='full')
    available_choices = (('yes', 'Yes'), ('no', 'No'))
    Available = models.CharField(max_length=10, choices=available_choices,default='no')
    essential_amenities=(('parking','Car parking'),
                         ('security','Security services'),
                         ('water','Water supply'),
                         ('elevator','Elevators'),
                         ('power','Power backup'),
                         ('maintenance','24-hour maintenance'))
    essentialamenities=MultiSelectField(choices=essential_amenities,default='parking')
    optional_amenities=(('play','Play area'),
                        ('gym','Gym'),
                        ('salon','Spa and salon'),
                        ('Concierge','Concierge services'),
                        ('hospital','Hospitals'),
                        ('restaurant','Restaurants'),
                        ('temples','Temple and religious activity place'),
                        ('wifi','Wi-Fi connectivity'))
    optionalamenities=MultiSelectField(choices=optional_amenities,default='play')
    description = models.TextField(blank=False,null=True)

    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    image1 = models.ImageField(upload_to=upload_location,verbose_name='Image(optional)', blank=True)
    image2 = models.ImageField(upload_to=upload_location, verbose_name='Image(optional)', blank=True)
    image3 = models.ImageField(upload_to=upload_location, verbose_name='Image(optional)', blank=True)
    image4 = models.ImageField(upload_to=upload_location, verbose_name='Image(optional)', blank=True)
    image5 = models.ImageField(upload_to=upload_location, verbose_name='Image(optional)', blank=True)
    image6 = models.ImageField(upload_to=upload_location, verbose_name='Image(optional)', blank=True)
    def get_absolute_url(self):
        return reverse("house-detail" ,kwargs={"my_id":self.id})
        return f"/question_list/{self.id}/"

    class Meta:
        ordering=["-updated","-timestamp"]

class share_room_Images(models.Model):
    sharedroom = models.ForeignKey(shared_room, default=None ,on_delete=models.CASCADE,)
    image = models.ImageField(upload_to=upload_location,
                              verbose_name='Image(optional)',blank=True
                              )

class question(models.Model):
    title = models.CharField(max_length=120)
    height_field=models.IntegerField(default=0)
    width_field=models.IntegerField(default=0)
    description = models.TextField(blank=False,null=True)
    user=models.CharField(max_length=120,null=True)
    updated=models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    tags = TaggableManager(blank=True)
    image1 = models.ImageField(upload_to=upload_location,
                              verbose_name='Image(optional)', blank=True
                              )
    def get_absolute_url(self):
        return reverse("question-detail" ,kwargs={"my_id":self.id})
        return f"/question_list/{self.id}/"

    class Meta:
        ordering=["-updated","-timestamp"]

class Images(models.Model):
    questionn = models.ForeignKey(question, default=None ,on_delete=models.CASCADE,)
    image = models.ImageField(upload_to=upload_location,
                              verbose_name='Image(optional)',blank=True
                              )
    #i_id=models.IntegerField(default=0)

'''class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=50)
    sex = models.CharField(max_length=1)'''

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

