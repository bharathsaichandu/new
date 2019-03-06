
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import formset_factory
from django.forms import modelformset_factory
from .models import question,Images,shared_room,share_room_Images,private_room,private_room_Images,entire_house,entire_house_Images
from taggit.forms import *

class entirehouseform(forms.ModelForm):
    user_name=forms.CharField(label='',widget=forms.HiddenInput(),required=False)
    user = forms.CharField(label='owner name', widget=forms.TextInput(attrs={"placeholder": "owner name",'style': 'width:500px'}), required=True)
    email = forms.EmailField(label='Email',widget=forms.TextInput(attrs={"placeholder": "email",'style': 'width:500px'}), required=True)
    City = forms.CharField(label='city', widget=forms.TextInput(attrs={"placeholder": "city",'style': 'width:500px'}), required=True)
    Area = forms.CharField(label='area name', widget=forms.TextInput(attrs={"placeholder": "area",'style': 'width:500px'}), required=True)
    Address = forms.CharField(label='address',widget=forms.TextInput(attrs={"placeholder": "address",'style': 'width:500px'}), required=True)
    house_type=(('flat','flat'),('seperate house','seperate house'))
    house=forms.ChoiceField(label="house type", initial='flat', widget=forms.Select(attrs={'style': 'width:500px'}), required=True,
                                  choices=house_type)
    rent = forms.IntegerField(label='rent', widget=forms.NumberInput(attrs={'style':'width:500px'}),required=True)
    securitydeposit = forms.IntegerField(label='security deposit', widget=forms.NumberInput(attrs={"placeholder": "in months",'style':'width:500px'}), required=True)
    Numbers = [(i, i) for i in range(11)]
    kitchen=forms.ChoiceField(label='kitchen',choices=Numbers,widget=forms.Select(attrs={'style': 'width:500px'}))
    hall=forms.ChoiceField(label='hall',choices=Numbers,widget=forms.Select(attrs={'style': 'width:500px'}))
    #rooms_available=forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": "number of rooms available",'style': 'width:500px'}),required=True)
    gender_choices=(('male','male'),('female','female'),('family','family'),('any','any'))
    gender = forms.ChoiceField(label="gender", initial='any', widget=forms.Select(attrs={'style': 'width:500px'}), required=True,
                                  choices=gender_choices)
    bed_rooms=forms.ChoiceField(label='bed rooms',choices=Numbers,widget=forms.Select(attrs={'style': 'width:500px'}))
    bathrooms=forms.ChoiceField(label='bath rooms',choices=Numbers,widget=forms.Select(attrs={'style': 'width:500px'}))
    Area_sqft=forms.IntegerField(widget=forms.NumberInput(attrs={'style':'width:500px'}))
    Furniture_choices = (('full', 'full furnished'), ('semi', 'semi furnished'), ('no', 'no furnished'))
    Furniture = forms.ChoiceField(label="furniture", initial='', widget=forms.Select(attrs={'style': 'width:500px'}), required=True,
                                  choices=Furniture_choices)
    essential_amenities = (('parking', 'Car parking'),
                           ('security', 'Security services'),
                           ('water', 'Water supply'),
                           ('elevator', 'Elevators'),
                           ('power', 'Power backup'),
                           ('maintenance', '24-hour maintenance'))
    essentialamenities = forms.MultipleChoiceField(label='essential amenities', initial='',
                                                   widget=forms.CheckboxSelectMultiple(), choices=essential_amenities)
    optional_amenities = (('play', 'Play area'),
                          ('gym', 'Gym'),
                          ('salon', 'Spa and salon'),
                          ('Concierge', 'Concierge services'),
                          ('hospital', 'Hospitals'),
                          ('restaurant', 'Restaurants'),
                          ('temples', 'Temple and religious activity place'),
                          ('wifi', 'Wi-Fi connectivity'))
    available_choices = (('yes', 'Yes'), ('no', 'No'))
    Available =forms.ChoiceField(label="house available", initial='', widget=forms.Select(attrs={'style': 'width:500px'}), required=True,
                                  choices=available_choices)

    optionalamenities = forms.MultipleChoiceField(label='optional amenities', initial='',
                                                  widget=forms.CheckboxSelectMultiple(), choices=optional_amenities)

    #otheramenities=TagField(label='other amenities',widget=models.TextField(blank=False, null=True)
    description = forms.CharField(label='Any details',widget=forms.Textarea(attrs={'style': 'width:500px'}),required=False)
    image1 = forms.ImageField(label='Image(optional)', required=False)
    image2 = forms.ImageField(label='Image(optional)', required=False)
    image3 = forms.ImageField(label='Image(optional)', required=False)
    image4 = forms.ImageField(label='Image(optional)', required=False)
    image5 = forms.ImageField(label='Image(optional)', required=False)
    image6 = forms.ImageField(label='Image(optional)', required=False)

    class Meta:
        model=entire_house
        fields=['user_name','user','email','Address','Area','City','house',
                'rent','securitydeposit','Available','bed_rooms',
                'bathrooms','kitchen','hall','Area_sqft','gender','Furniture',
                'essentialamenities','optionalamenities','description','image1','image2','image3','image4','image5','image6'
                ]
        widgets = {'user_name': forms.HiddenInput()}


class privateroomform(forms.ModelForm):
    user_name=forms.CharField(label='',widget=forms.HiddenInput(),required=False)
    user = forms.CharField(label='owner name', widget=forms.TextInput(attrs={"placeholder": "owner name",'style': 'width:500px'}), required=True)
    email = forms.EmailField(label='Email',widget=forms.TextInput(attrs={"placeholder": "email",'style': 'width:500px'}), required=True)
    City = forms.CharField(label='city', widget=forms.TextInput(attrs={"placeholder": "city",'style': 'width:500px'}), required=True)
    Area = forms.CharField(label='area name', widget=forms.TextInput(attrs={"placeholder": "area",'style': 'width:500px'}), required=True)
    Address = forms.CharField(label='address',widget=forms.TextInput(attrs={"placeholder": "address",'style': 'width:500px'}), required=True)
    rent = forms.IntegerField(label='rent', widget=forms.NumberInput(attrs={'style':'width:500px'}),required=True)
    securitydeposit = forms.IntegerField(label='security deposit', widget=forms.NumberInput(attrs={"placeholder": "in months",'style':'width:500px'}), required=True)
    Numbers = [(i, i) for i in range(11)]
    kitchen=forms.ChoiceField(label='kitchen',choices=Numbers,widget=forms.Select(attrs={'style': 'width:500px'}))
    hall=forms.ChoiceField(label='hall',choices=Numbers,widget=forms.Select(attrs={'style': 'width:500px'}))
    rooms_available=forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": "number of rooms available",'style': 'width:500px'}),required=True)
    gender_choices=(('male','male'),('female','female'),('family','family'),('any','any'))
    gender = forms.ChoiceField(label="gender", initial='any', widget=forms.Select(attrs={'style': 'width:500px'}), required=True,
                                  choices=gender_choices)
    bed_rooms=forms.ChoiceField(label='bed rooms',choices=Numbers,widget=forms.Select(attrs={'style': 'width:500px'}))
    bathrooms=forms.ChoiceField(label='bath rooms',choices=Numbers,widget=forms.Select(attrs={'style': 'width:500px'}))
    Area_sqft=forms.IntegerField(widget=forms.NumberInput(attrs={'style':'width:500px'}))
    Furniture_choices = (('full', 'full furnished'), ('semi', 'semi furnished'), ('no', 'no furnished'))
    Furniture = forms.ChoiceField(label="furniture", initial='', widget=forms.Select(attrs={'style': 'width:500px'}), required=True,
                                  choices=Furniture_choices)
    essential_amenities = (('parking', 'Car parking'),
                           ('security', 'Security services'),
                           ('water', 'Water supply'),
                           ('elevator', 'Elevators'),
                           ('power', 'Power backup'),
                           ('maintenance', '24-hour maintenance'))
    essentialamenities = forms.MultipleChoiceField(label='essential amenities', initial='',
                                                   widget=forms.CheckboxSelectMultiple(), choices=essential_amenities)
    optional_amenities = (('play', 'Play area'),
                          ('gym', 'Gym'),
                          ('salon', 'Spa and salon'),
                          ('Concierge', 'Concierge services'),
                          ('hospital', 'Hospitals'),
                          ('restaurant', 'Restaurants'),
                          ('temples', 'Temple and religious activity place'),
                          ('wifi', 'Wi-Fi connectivity'))
    available_choices = (('yes', 'Yes'), ('no', 'No'))
    Available =forms.ChoiceField(label="rooms available", initial='', widget=forms.Select(attrs={'style': 'width:500px'}), required=True,
                                  choices=available_choices)

    optionalamenities = forms.MultipleChoiceField(label='optional amenities', initial='',
                                                  widget=forms.CheckboxSelectMultiple(), choices=optional_amenities)

    #otheramenities=TagField(label='other amenities',widget=models.TextField(blank=False, null=True)
    description = forms.CharField(label='Any details',widget=forms.Textarea(attrs={'style': 'width:500px'}),required=False)
    image1 = forms.ImageField(label='Image(optional)', required=False)
    image2 = forms.ImageField(label='Image(optional)', required=False)
    image3 = forms.ImageField(label='Image(optional)', required=False)
    image4 = forms.ImageField(label='Image(optional)', required=False)
    image5 = forms.ImageField(label='Image(optional)', required=False)
    image6 = forms.ImageField(label='Image(optional)', required=False)

    class Meta:
        model=private_room
        fields=['user_name','user','email','Address','Area','City',
                'rent','securitydeposit','Available','bed_rooms',
                'bathrooms','kitchen','hall','rooms_available','Area_sqft','gender','Furniture',
                'essentialamenities','optionalamenities','description','image1','image2','image3','image4','image5','image6'
                ]
        widgets = {'user_name': forms.HiddenInput()}


class sharedroomform(forms.ModelForm):
    user_name=forms.CharField(label='',widget=forms.HiddenInput(),required=False)
    user = forms.CharField(label='owner name', widget=forms.TextInput(attrs={"placeholder": "owner name",'style': 'width:500px'}), required=True)
    email = forms.EmailField(label='Email',widget=forms.TextInput(attrs={"placeholder": "email",'style': 'width:500px'}), required=True)
    City = forms.CharField(label='city', widget=forms.TextInput(attrs={"placeholder": "city",'style': 'width:500px'}), required=True)
    Area = forms.CharField(label='area name', widget=forms.TextInput(attrs={"placeholder": "area",'style': 'width:500px'}), required=True)
    Address = forms.CharField(label='address',widget=forms.TextInput(attrs={"placeholder": "address",'style': 'width:500px'}), required=True)
    rent = forms.IntegerField(label='rent', widget=forms.NumberInput(attrs={'style':'width:500px'}),required=True)
    securitydeposit = forms.IntegerField(label='security deposit', widget=forms.NumberInput(attrs={"placeholder": "in months",'style':'width:500px'}), required=True)
    Numbers = [(i, i) for i in range(11)]
    kitchen=forms.ChoiceField(label='kitchen',choices=Numbers,widget=forms.Select(attrs={'style': 'width:500px'}))
    hall=forms.ChoiceField(label='hall',choices=Numbers,widget=forms.Select(attrs={'style': 'width:500px'}))
    beds_available=forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": "number of beds available",'style': 'width:500px'}),required=True)
    gender_choices=(('male','male'),('female','female'),('family','family'),('any','any'))
    gender = forms.ChoiceField(label="gender", initial='any', widget=forms.Select(attrs={'style': 'width:500px'}), required=True,
                                  choices=gender_choices)
    bed_rooms=forms.ChoiceField(label='bed rooms',choices=Numbers,widget=forms.Select(attrs={'style': 'width:500px'}))
    bathrooms=forms.ChoiceField(label='bath rooms',choices=Numbers,widget=forms.Select(attrs={'style': 'width:500px'}))
    Area_sqft=forms.IntegerField(widget=forms.NumberInput(attrs={'style':'width:500px'}))
    Furniture_choices = (('full', 'full furnished'), ('semi', 'semi furnished'), ('no', 'no furnished'))
    Furniture = forms.ChoiceField(label="furniture", initial='', widget=forms.Select(attrs={'style': 'width:500px'}), required=True,
                                  choices=Furniture_choices)
    essential_amenities = (('parking', 'Car parking'),
                           ('security', 'Security services'),
                           ('water', 'Water supply'),
                           ('elevator', 'Elevators'),
                           ('power', 'Power backup'),
                           ('maintenance', '24-hour maintenance'))
    essentialamenities = forms.MultipleChoiceField(label='essential amenities', initial='',
                                                   widget=forms.CheckboxSelectMultiple(), choices=essential_amenities)
    optional_amenities = (('play', 'Play area'),
                          ('gym', 'Gym'),
                          ('salon', 'Spa and salon'),
                          ('Concierge', 'Concierge services'),
                          ('hospital', 'Hospitals'),
                          ('restaurant', 'Restaurants'),
                          ('temples', 'Temple and religious activity place'),
                          ('wifi', 'Wi-Fi connectivity'))
    available_choices = (('yes', 'Yes'), ('no', 'No'))
    Available =forms.ChoiceField(label="beds available", initial='', widget=forms.Select(attrs={'style': 'width:500px'}), required=True,
                                  choices=available_choices)

    optionalamenities = forms.MultipleChoiceField(label='optional amenities', initial='',
                                                  widget=forms.CheckboxSelectMultiple(), choices=optional_amenities)

    #otheramenities=TagField(label='other amenities',widget=models.TextField(blank=False, null=True)
    description = forms.CharField(label='Any details',widget=forms.Textarea(attrs={'style': 'width:500px'}),required=False)
    image1 = forms.ImageField(label='Image(optional)', required=False)
    image2 = forms.ImageField(label='Image(optional)', required=False)
    image3 = forms.ImageField(label='Image(optional)', required=False)
    image4 = forms.ImageField(label='Image(optional)', required=False)
    image5 = forms.ImageField(label='Image(optional)', required=False)
    image6 = forms.ImageField(label='Image(optional)', required=False)
    class Meta:
        model=shared_room
        fields=['user','email','Address','Area','City',
                'rent','securitydeposit','Available','bed_rooms',
                'bathrooms','kitchen','hall','beds_available','Area_sqft','gender','Furniture',
                'essentialamenities','optionalamenities','description','image1','image2','image3','image4','image5','image6'
                ]
        widgets = {'user_name': forms.HiddenInput()}
class questionForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your description",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 10,
                'cols': 100,
            }
        )
    )
    user=forms.CharField(widget=forms.HiddenInput(),required=False)
    image1 = forms.ImageField(label='Image(optional)',required=False)


    class Meta:
        model = question
        fields = [
            'title',
            'description',
            'user',
            'image1',
            'tags',

        ]
        #fields = "__all__"
        widgets={'user':forms.HiddenInput()}

class shareImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image(optional)')
    i_id=forms.IntegerField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model = share_room_Images
        fields = ('image', )

class entirehouseImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image(optional)')
    i_id=forms.IntegerField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model = entire_house_Images
        fields = ('image', )

class privateImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image(optional)')
    i_id=forms.IntegerField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model = private_room_Images
        fields = ('image', )

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image(optional)')
    i_id=forms.IntegerField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model = Images
        fields = ('image', )

#FestivalAddressFormSet = inlineformset_factory(FestivalForm, FestivalAddress, form=FestivalAddressForm, extra=2)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class SearchForm(forms.Form):
    city = forms.CharField(label='',
                            widget=forms.TextInput(attrs={"placeholder": "enter city"}))
    area = forms.CharField(label='',
                            widget=forms.TextInput(attrs={"placeholder": "enter area"}))

    class Meta:
        model = question
        fields = [
            'city',
            'area'

        ]
        #fields = "__all__"
        widgets={'user':forms.HiddenInput()}


'''class ModuleForm(forms.Form):
    release_num = forms.ModelChoiceField(queryset=Release.objects.all(), empty_label='Pick a Release')
    metamodule_name = forms.ModelChoiceField(queryset=Metamodule.objects.all(), empty_label='Pick a Meta module')
    module_name = forms.ModelChoiceField(queryset=Module.objects.all(), empty_label='Pick a Module')

    def clean_release_number(self):
        try:
            release_num = self.cleaned_data.get["release_num"]
            metamodule_name = int(self.cleaned_data["metamodule_name"])
            module_name = int(self.cleaned_data["module_name"])
        except:
            release_num = None
            metamodule_name = None
            module_name = None

        if release_num and Module.objects.exclude(metamodule__release__number=release_num).exists():
            raise forms.ValidationError("Please enter a valid release number.")
        else:
            return release_num'''