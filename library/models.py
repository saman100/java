from django.db import models
from django.urls import reverse
from django.conf import settings



class Book(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    publish_date=models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    LOAN_STATUS = (
        ('a', 'Adventure'),
        ('c', 'Classics'),
        ('f', 'Fantasy'),
        ('h', 'Horror'),
    )

    category = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='a', help_text='Book availability')



    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title


    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('book-detail', args=[str(self.id)])
