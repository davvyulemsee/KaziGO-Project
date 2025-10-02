from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Users(AbstractUser):
    SKILL_CHOICES = [
        ('WD', 'Web Development'),
        ('GD', 'Graphic Design'),
        ('WR', 'Writing & Translation'),
        ('DM', 'Digital Marketing'),
        ('VA', 'Virtual Assistant'),
        ('VO', 'Voice Over'),
        ('SE', 'SEO'),
        ('DA', 'Data Analysis'),
    ]


    profile_image = models.ImageField(default='default.jpg', blank=True)
    bio = models.TextField(max_length=500, blank=True)
    is_seller = models.BooleanField(default=False)
    skills = models.CharField(max_length=10, choices=SKILL_CHOICES, blank=True)

    def __str__(self):
        return self.username

