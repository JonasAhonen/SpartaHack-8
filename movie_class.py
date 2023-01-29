#Class structure for movie
import csv

class Movie:
  def __init__(self, film_title, release_year, director, cast, personal_rating, average_rating, url):
    self.film_title = film_title
    self.release_year = release_year
    self.director = director
    self.cast = cast
    self.personal_rating = personal_rating
    self.average_rating = average_rating
    self.url = url

  def __str__(self):
    #return self.film_title
    #return str(self.release_year)
    #return self.director
    #return str(self.cast)
    #return self.personal_rating
    #return str(self.average_rating) 
    #return self.url
    return f'{self.film_title} ({str(self.release_year)})\n{self.director}'