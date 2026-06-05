from django.db import models

# Create your models here.

class Food(models.Model):
    DIETTYPE_CHOICES = [
        ('VEGAN', 'VEGAN'),
        ('VEGETARIAN', 'VEGETARIAN'),
        ('KETO', 'KETO'),
        ('NONE', 'NONE'),
    ]

    name = models.CharField(max_length=35)
    shortDescription = models.CharField(max_length=256)
    longDescription = models.TextField()
    dietType = models.CharField(max_length=20, choices=DIETTYPE_CHOICES, default='NONE')
    mainImage = models.ImageField(upload_to='foods/', blank=True, null=True)
    brandId = models.IntegerField()
    brandName = models.CharField(max_length=35)
    rating = models.IntegerField()
    originalPrice = models.IntegerField()
    discountPrice = models.IntegerField()
    weight = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name

class FoodImage(models.Model):
    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField(upload_to='foods/')
