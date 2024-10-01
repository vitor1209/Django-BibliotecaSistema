"""
Configuração de URL para projeto de configuração.

A lista `urlpatterns` roteia URLs para visualizações. Para mais informações consulte:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Exemplos:
Visualizações de função
    1. Adicione uma importação: das visualizações de importação my_app
    2. Adicione um URL aos urlpatterns: path('', views.home, name='home')
Visualizações baseadas em classe
    1. Adicione uma importação: from other_app.views import Home
    2. Adicione um URL aos urlpatterns: path('', Home.as_view(), name='home')
Incluindo outro URLconf
    1. Importe a função include(): from django.urls import include, path
    2. Adicione um URL aos urlpatterns: path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from todos.views import BibliotecaListView, BibliotecaCreateView, BibliotecaUpdateView , BibliotecaDeleteView ,BibliotecaTimeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", BibliotecaListView.as_view(), name="livros_list"),
    path("create", BibliotecaCreateView.as_view(), name="livros_create"),
    path("update/<int:pk>", BibliotecaUpdateView.as_view(), name="livros_Update"),
    path("delete/<int:pk>" , BibliotecaDeleteView.as_view(), name="livros_Delete"),
    path("complete/<int:pk>" , BibliotecaTimeView.as_view(), name="livros_Time"),   
]
