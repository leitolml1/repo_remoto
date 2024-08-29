from django.shortcuts import render,redirect,get_object_or_404
from .forms import CrearPost,AgregarComentario
from .models import Post,Comment
# Create your views here.

def base(request):
    return render(request,"base.html",{

    })

def post_list(request):
    posts=Post.objects.all()
    return render(request,"POST/post_list.html",{
        "posts":posts
    }
    )
def crear_post(request):
    formCrearPost=CrearPost()
    if request.method=="POST":
        form=CrearPost(request.POST)
        if form.is_valid():
            nuevoPOST=form.save(commit=False)
            nuevoPOST.save()
        return redirect("post_list")
    else:
        return render(request,"POST/crearPOST.html",{
            "formCrearPost":formCrearPost
        })
def detalle_post(request,id):
    if request.method=="GET":
        post=get_object_or_404(Post,id=id)
        comentarios=Comment.objects.filter(post=post)
        return render(request,"POST/post_detail.html",{
                "post":post,
                "comentarios":comentarios
        })
def editar_post(request,id):
    post=get_object_or_404(Post,id=id)
    if request.method=="POST":
        instanciar_form=CrearPost(request.POST,instance=post)
        if instanciar_form.is_valid():
            instanciar_form.save()
            return redirect("post_list")
    else:
        instanciar_form=CrearPost(instance=post)
    return render(request,"POST/post_edit.html",{
        "form":instanciar_form
    })  

def agregarComentario(request,id):
    if request.method=="POST":
        form=AgregarComentario(request.POST)
        if form.is_valid():
            post=get_object_or_404(Post,id=id)
            nuevoComentario=form.save(commit=False)
            nuevoComentario.post=post
            nuevoComentario.save()
        return redirect("detalle_post",id=id)
    else:
        return render(request,"POST/agregarComentario.html",{
            "form":AgregarComentario()
        })