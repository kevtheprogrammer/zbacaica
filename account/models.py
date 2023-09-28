from __future__ import unicode_literals
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.urls import reverse

 
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    email = models.EmailField(verbose_name='email address', unique=True)
    first_name = models.CharField(
        verbose_name='first name', max_length=30, blank=True)
    last_name = models.CharField(verbose_name='last name', max_length=30, blank=True)
    dob = models.DateField(auto_now=True, blank=True)
    nrc = models.CharField(verbose_name='national registration number', max_length=300, blank=True)
    country = CountryField(blank_label='(select country)', blank=True)
    phone =  PhoneNumberField(blank=True)
    is_staff = models.BooleanField(verbose_name='staff', default=False)
    location = models.CharField(verbose_name='location', max_length=50, blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='active', default=True)
    is_verified = models.BooleanField(verbose_name='verified', default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        
    def get_status(self):
        if self.is_active:
            return 'Active'
        return 'Not Active'

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        print(subject, message, from_email,)
        # send_mail(subject, message, from_email, [self.email], **kwargs)
    
    # def get_absolute_url(self):
    #     return reverse('account:profile', args=[self.pk])

    # def get_edit_url(self):
    #     return reverse('account:profile-edit', args=[self.pk])
    
    # def get_soil_url(self):
    #     return reverse('account:soil',args=[self.pk])
    

class Category(models.Model):
    thumb  = models.ImageField( upload_to='category/thumb/',default="thumb.jpg" )
    title  = models.CharField(max_length=9000)
    body   = models.TextField( default=None,verbose_name="content",blank = True )
    slug   = models.SlugField( default=None )
    l_updated   = models.DateField( auto_now=True )

    def __str__(self) -> str:
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse('products:category', args=[self.slug,self.pk])

class Product(models.Model):
    thumb  = models.ImageField( upload_to='products/thumb/',default="thumb.jpg" )
    title  = models.CharField( max_length=9000,default=None )
    body   = models.TextField( default=None,verbose_name="content",blank = True )
    author = models.ForeignKey( User,on_delete=models.CASCADE,default=None,related_name="author" )
    categpry = models.ForeignKey( Category,on_delete=models.CASCADE,default=None,related_name="category" )
    slug   = models.SlugField( default=None )
    stamp  = models.DateField( auto_now_add=True )
    l_updated   = models.DateField( auto_now=True )
    
    def __str__(self) -> str:
        return f"{self.title}"

    def snip(self):
        return f'{self.body[:50]} ...'
    
    class Meta: 
        ordering = ('-stamp',) 

class Review(models.Model): 
    name    = models.CharField(max_length=80) 
    email   = models.EmailField() 
    body    = models.TextField() 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 

    class Meta: 
        ordering = ('-created',) 

    def __str__(self): 
        return 'contact by {}'.format(self.name,) 