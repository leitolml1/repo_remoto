from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.base,name="home"),
    path('post_list/',views.post_list,name="post_list"),
    path('post_list/crearPOST',views.crear_post,name="crear_post"),
    path('post_list/postDetalle/<int:id>',views.detalle_post,name="detalle_post"),
    path('post_list/postEditar/<int:id>',views.editar_post,name="editar_post"),
    path('post_list/agregarComentario/<int:id>',views.agregarComentario,name="agregarComentario"),
]
