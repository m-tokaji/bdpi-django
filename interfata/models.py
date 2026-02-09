from django.db import models






class Genres(models.Model):
    id = models.BigAutoField(primary_key=True)
    genre_name = models.CharField(max_length=255, blank=False, null=False)

    labels={ 'genre_name': 'nume'}



    class Meta:
        managed = False
        db_table = 'genres'

    def  __str__(self):
        return self.genre_name

class Books(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    book_name = models.CharField(max_length=255, blank=False, null=True)
    release_date = models.IntegerField(blank=True, null=True)
    selids = models.JSONField(blank=True, null=True)

    labels = {
            'book_name': 'Titlu',
            'author': 'Autor',
            'release_date': 'An lansare',
            'genres': 'Genuri'
        }

    genres=models.ManyToManyField( Genres , through='Relation', related_name='books', blank=True )

    class Meta:
        managed = False
        db_table = 'books'



class Relation(models.Model):
    id = models.BigAutoField(primary_key=True)
    book = models.ForeignKey(Books, models.CASCADE, blank=True, null=True)
    genre = models.ForeignKey(Genres, models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'relation'
