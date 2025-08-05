from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """Custom user manager for email-based authentication."""

    def create_user(self, email, password=None, **extra_fields):
        """Create and return a regular user with an email and password."""
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a superuser with an email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    Custom User model that uses email as the username field.

    This gives us flexibility to add custom fields in the future
    while maintaining all the default Django user functionality.
    """

    # Make email required and unique
    email = models.EmailField(
        unique=True,
        help_text='Required. Enter a valid email address.'
    )

    # Make username optional but still available
    username = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        help_text='Optional. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
    )

    # Set email as the username field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Remove username from required fields since email is the login

    objects = UserManager()

    # Add any custom fields here as needed
    # Example fields you might want to add later:
    # phone_number = models.CharField(max_length=20, blank=True)
    # date_of_birth = models.DateField(null=True, blank=True)
    # profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    # is_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'auth_user'  # Use the same table name as Django's default User
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        """Return the user's full name."""
        return f"{self.first_name} {self.last_name}".strip()
