def cantidadProductosCarro(request):
    total1=0
    for key, value in request.session["carro"].items():
        print("safadfasfasd", value, total1)
        total1+=1
        print("tosafklasdfsd", total1)
    return {"cantidadProductosCarro":total1}



def importeTotalCarro(request):
    total=0
    c=0
    # if request.user.is_authenticated:
    # if 'cart' in request.session:
    for key, value in request.session["carro"].items():
        total= total + (float(value["precio"]))
        c=c+1
    return {"importeTotalCarro":total}

