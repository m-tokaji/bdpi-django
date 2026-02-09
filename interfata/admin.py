from django.contrib import admin
from .models import Books,Genres,Relation

admin.site.register(Books)
admin.site.register(Genres)
admin.site.register(Relation)

# Register your models here.
