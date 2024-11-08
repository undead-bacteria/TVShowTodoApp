from django.db import models


class TelevisionShow(models.Model):

  GENRE_CHOICES = [
    ('Drama', 'Drama'),
    ('Comedy', 'Comedy'),
    ('Thriller', 'Thriller'),
    # Add more genres here...
  ]
  
  title = models.CharField(
    max_length=200, 
    verbose_name="Title", 
  )
  genre = models.CharField(
    max_length=200,
    choices=GENRE_CHOICES, 
    verbose_name="Genre", 
  )
  release_date = models.DateField(
    verbose_name="Release Date", 
  ) 
  description = models.TextField(
    blank=True, 
    verbose_name="Description", 
  ) 

  def __str__(self):
    """
    Return the title of the show when it's displayed in the admin panel
    or anywhere the object is printed.
    """
    return self.title
  
  class Meta:
    # Set a more readable singular name for the model
    verbose_name = "Television Show"
    verbose_name_plural = "Television Shows"

    #ordering by release date
    ordering = ['release_date']

    # Adding an index for better performance when filtering by genre or release date.
    indexes = [
      models.Index(fields=['genre']),
      models.Index(fields=['release_date']),
    ]

    # Ensuring that the title of the show is unique to avoid duplicates.
    unique_together = ['title']
  

