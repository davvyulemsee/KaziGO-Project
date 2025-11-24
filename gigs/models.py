from django.db import models
from django.conf import settings

# Create your models here.

class Gig(models.Model):
    CATEGORY_CHOICES = [
        ('EL', 'Electrician'),
        ('PB', 'Plumbing repairs'),
        ('MV', 'Moving'),
        ('GD', 'Gardening'),
        ('CL', 'Cleaning'),
        ('CP', 'Carpentry'),
        ('HR', 'Home Repairs'),
        ('VA', 'Virtual Assistant'),
    ]

    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='gigs')
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='gig_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Gig.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} by {self.seller.username}"


from django.db import models

class TaskRequest(models.Model):
    category = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    details = models.TextField()
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='task_requests', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} task at {self.location}"

    
