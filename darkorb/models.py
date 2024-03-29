from django.db import models

# Create your models here.
# class Movie(models.Model):

class Movie:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self, id, title, overview, poster, vote_average, vote_count, age, release_date, original_language):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count
        self.age = age
        self.release_date = original_language
        self.original_language = original_language