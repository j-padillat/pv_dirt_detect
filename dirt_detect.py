import random
xmin = 377
ymin=691
xmax=1012
ymax=1420
esquina_infIz=[xmin,ymax]
esquina_infDe=[xmax,ymax]
esquina_supDe=[xmax,ymin]
esquina_supIz=[xmin,ymin]

posicion=[esquina_infDe[0]-12,esquina_infDe[0]-8]


puntoSucio=[random.randint(xmin,xmax),random.randint(ymin,ymax)]
print(puntoSucio)
print(posicion)
bandera=False # Si está False significa que estámos buscando suciedad de manera vertical osea en el eje Y.
c=0
limpia=False
if not bandera:
	# Se hace la busqueda vertical con la longitud del robot y si el punto sucion está en el rango entre posicion en eje x y posicion + longitud entonces retorna un 1; si no sigue en cero.
	while c!=7:

	if (posicion[0]<puntoSucio[0])and (puntoSucio[0]<posicion[0]+longitud):
		limpia=True
	else:
		limpia=False
	
	c+=1
