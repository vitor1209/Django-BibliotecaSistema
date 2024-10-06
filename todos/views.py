from django.views.generic import ListView, CreateView, UpdateView , DeleteView , View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from .models import livros

class BibliotecaListView(ListView):
    model = livros
    template_name = "todos/livrosLista.html"


class BibliotecaCreateView(CreateView):
    model = livros
    template_name = "todos/livrosForms.html"
    fields = ["titulo", "autor", "genero", "anoPublicacao"]
    success_url = reverse_lazy("livros_list")


class BibliotecaUpdateView(UpdateView):
    model = livros
    template_name = "todos/livrosForms.html"
    livros.dataDevol = None
    fields = ["dataAlugou", "nomeAlugou", "telefoneAlugou"]
    success_url = reverse_lazy("livros_list")

class BibliotecaDeleteView(DeleteView):
    model = livros
    template_name = "todos/livroDelete.html"
    success_url = reverse_lazy("livros_list")

class BibliotecaTimeView(View):
    def get(self , request , pk):
         livro = get_object_or_404(livros , pk=pk)
         livro.markTime()
         return redirect("livros_list")