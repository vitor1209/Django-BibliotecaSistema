from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import livros


class BibliotecaListView(ListView):
    model = livros
    template_name = "todos/livrosLista.html"


class BibliotecaCreateView(CreateView):
    model = livros
    template_name = "todos/livrosForms.html"
    fields = ["titulo", "autor", "genero", "anoPublicacao"]
    success_url = reverse_lazy("livros_list")
