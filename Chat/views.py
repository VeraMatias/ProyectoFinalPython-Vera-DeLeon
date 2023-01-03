from django.shortcuts import redirect, render
from Chat.forms import ChatForm
from Usuario.models import Avatar
from .models import Mensaje
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

#Definciones de Funciones
def ObtenerUsuarios(chats,Userid):
    lista_mensajes = list(chats.values_list('emisor', 'receptor')) #armo lista de tuplas con id de emisor y receptor

    lista_mensajes = list(set(lista_mensajes)) #elimino repetidos

    usuarios = list()
    for elemento in lista_mensajes:
        elemento = list(elemento)
        if elemento[1] == Userid: # si user es el receptor, guardo id emisor
            if elemento[0] not in usuarios: #guardo el id del receptor solo si no esta guardado
                usuarios.append(elemento[0])
        else:
            if elemento[1] not in usuarios: # si user es emisor guardo el id del receptor solo si no esta guardado
                usuarios.append(elemento[1])
    usuarios.sort()

    return usuarios

def ObtenerAvatares(id_usuarios):
    avatares =[]
    for id in id_usuarios:
        lista=Avatar.objects.filter(user_id=id)
        if len(lista)!=0:
            imagen=lista[0].imagen.url
        else:
            imagen="../../media/avatares/avatarpordefecto.png"
        avatares.append(imagen) 
    return avatares

def MarcarLeidos(mensajes):
    for mensaje in mensajes:
        mensaje.leido = True
        mensaje.save()
    return mensajes

# Create your views here.
@login_required
def inicio(request):
    
    chats = Mensaje.objects.filter(emisor__id__icontains=request.user.id) | Mensaje.objects.filter(receptor__id__icontains=request.user.id) #Obtengo todos los chats que involucran al user
    id_usuarios = ObtenerUsuarios(chats,request.user.id)
    avatar_usuarios = ObtenerAvatares(id_usuarios)


    if len(id_usuarios) !=0:
        #Cargo todos los chats que tengo activos.
        usuarios = User.objects.filter(id=id_usuarios[0])

        for elemento in id_usuarios:
            usuarios |= User.objects.filter(id=elemento)

        fusion = zip(usuarios,avatar_usuarios)


        #Acciones a realizar cuando apreto un chat en particular
        if request.method=="POST":
            #Obtengo el id del usuario que estoy charlando
            receptor_id = request.POST['receptor_id']

            #Obtengo nombre del user que estoy charlando
            usuario_chat = User.objects.filter(id = receptor_id).first()

            #Obtengo el avatar del user que estoy charlando
            avatar_chat= ObtenerAvatares([receptor_id])[0]


            #Obtengo el historial de charla con el user y marco los msj recibidos como leidos
            historial = Mensaje.objects.filter(emisor__id=receptor_id, receptor__id=request.user.id) #mensajes recibidos
            historial = MarcarLeidos(historial)
            historial |= Mensaje.objects.filter(emisor__id=request.user.id, receptor__id = receptor_id) #agrego mensajes recibidos
            
            historial.order_by("-fecha")
            return render(request , "inicio_chat.html", {"fusion": fusion, "historial": historial, "usuario_chat": usuario_chat, "avatar_chat": avatar_chat})
        
        return render(request , "inicio_chat.html", {"fusion":fusion})
    else:
        return render(request , "inicio_chat.html")

@login_required
def nuevochat(request):
    if request.method=="POST":
        form=ChatForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            Chat_a_Cargar=Mensaje(emisor=request.user,receptor = informacion["receptor"], mensaje= informacion["mensaje"], fecha = datetime.now(),leido = False)
            Chat_a_Cargar.save()
            #return render (request, "inicio_chat.html")
            return redirect('/Chat/inicio')
        else:
            return render(request, "nuevo_chat.html", {"form":form, "mensaje": "Error, mensajes no enviado."})
    else:
        form=ChatForm()
        return render(request , "nuevo_chat.html", {"form": form})

@login_required
def enviarmsj(request):
    if request.method=="POST":
        receptor = User.objects.filter(id = request.POST['receptor']).first()
        Chat_a_Cargar=Mensaje(emisor=request.user,receptor = receptor, mensaje= request.POST["mensaje"], fecha = datetime.now(),leido = False)
        Chat_a_Cargar.save()
        return redirect('/Chat/inicio')
    else:
        return render(request, "inicio_chat.html")
