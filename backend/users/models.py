from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    """
    Custom user model that extends Django's AbstractUser.
    Uses email as the primary login field while still requiring a username
    for display and compatibility with Django admin and other built-in features.

    Additional fields:
    - bio: Short user description
    - profile_image: Optional profile picture
    - github_link: Link to GitHub
    - reputation_score: Integer used for gamification / trust score
    """

    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    github_link = models.URLField(blank=True, null=True)
    reputation_score = models.IntegerField(default=0)

    # Use email as the unique identifier instead of username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-reputation_score']

    