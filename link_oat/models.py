from django.db import models


# Create your models here.
class Profile(models.Model):
    BG_CHOICES = (
        ("#ffffff", "White"),
        ("#000000", "Black"),
        ("#ff0000", "Red"),
        ("#00ff00", "Green"),
        ("#0000ff", "Blue"),
        ("#ffff00", "Yellow"),
        ("#00ffff", "Cyan"),
        ("#ff00ff", "Magenta"),
    )

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    bg_color = models.CharField(max_length=7, choices=BG_CHOICES, default="#ffffff")

    def __str__(self):
        return self.name

class Link(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="links")
    url = models.URLField(max_length=200)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text