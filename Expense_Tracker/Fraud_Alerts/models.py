from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # your custom fields here
    
    # Fix the reverse accessor conflicts
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='fraud_alerts_user_set',  # Custom related_name
        related_query_name='user',
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='fraud_alerts_user_set',  # Custom related_name
        related_query_name='user',
    )
