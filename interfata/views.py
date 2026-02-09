# core/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Books, Genres, Relation
from .forms import BookForm

class BookListView(ListView):
    model = Books
    template_name = 'interfata/books_list.html'



class BookCreateView(CreateView):
    model = Books
    form_class=BookForm
    template_name = 'interfata/add_books_form.html'
    success_url = reverse_lazy('book-list')

    def form_valid(self, form):
        self.object = form.save()

        return super().form_valid(form)

class BookUpdateView(UpdateView):
    model = Books
    form_class=BookForm
    template_name = 'interfata/update_books_form.html'
    success_url = reverse_lazy('book-list')

    def get_initial(self):
        initial = super().get_initial()
        initial['genres'] = self.object.genres.all()
        return initial

    def form_valid(self, form):
        
        self.object = form.save()

        
        Relation.objects.filter(book=self.object).delete()

     
        for genre in form.cleaned_data['genres']:
            Relation.objects.create(
                book=self.object,
                genre=genre
            )

        return super().form_valid(form)

    

class BookDeleteView(DeleteView):
    model = Books
    template_name = 'interfata/books_list.html'
    success_url = reverse_lazy('book-list')

class GenreListView(ListView):
    model=Genres
    template_name='interfata/genres_list.html'

class GenreCreateView(CreateView):
    model = Genres
    fields=['genre_name']
    template_name = 'interfata/genres_form.html'
    success_url = reverse_lazy('genres-list')

class GenreDeleteView(DeleteView):
    model= Genres
    template_name='interfata/genres_list.html'
    success_url=reverse_lazy('genres-list')

