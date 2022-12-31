from contextlib import nullcontext
from Blog.models import Post
from Usuario.models import Avatar


def ObtenerRecientes (request):
    recientes = Post.objects.all().order_by('-fecha')[:5]
    return {"recientes": recientes}

def ObtenerAvatar(request):
    if request.user.is_authenticated:
        lista=Avatar.objects.filter(user=request.user)
        if len(lista)!=0:
            imagen=lista[0].imagen.url
        else:
            imagen="../../media/avatares/avatarpordefecto.png"

        return {"avatar":imagen}
    else:
        imagen="../../media/avatares/avatarpordefecto.png"

        return {"avatar":imagen}

