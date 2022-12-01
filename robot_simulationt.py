import turtle
import time
import cv2
from PIL import Image
import random

# ---- Se ajusta el tamanio de la imagen a utilizar para el fondo ---
def resize_jpg(rutajpg,rutajpgresized,porcentaje_resize):

    image=cv2.imread(rutajpg)

    scale_percent=porcentaje_resize
    print(image.shape)
    width=int(image.shape[1]*scale_percent)

    height=int(image.shape[0]*scale_percent)

    dimension=(width,height)

    resized = cv2.resize(image,dimension, interpolation = cv2.INTER_AREA)

    print(resized.shape)

    cv2.imwrite(rutajpgresized,resized)
    return resized.shape[1],resized.shape[0]
# ----------------------------------------------------------------

# ---- Se guarda la imagen en formato .gif ---
def image_to_gif(rutajpgresized,rutagif):
    img = Image.open(rutajpgresized)
    img.save(rutagif)

def derecha():
    ventana.addshape("./images/robot_right.gif")
    tortuga.shape("./images/robot_right.gif")
def izquierda():
    ventana.addshape("./images/robot_left.gif")
    tortuga.shape("./images/robot_left.gif")
def abajo():
    ventana.addshape("./images/robot_down.gif")
    tortuga.shape("./images/robot_down.gif")
def arriba():
    ventana.addshape("./images/robot_up.gif")
    tortuga.shape("./images/robot_up.gif")
# -----------------------------------------------------------------
def ff():
    print(tortuga.pos())

if __name__ == "__main__":
    # ---- Se crean el fondo y la tortuga ---
    porcentaje_resize=1.4
    rutajpg="./images/panelDeteccion.png"
    rutajpgresized="./images/panel_2.jpg"
    ancho_ventana,alto_ventana=resize_jpg(rutajpg,rutajpgresized,porcentaje_resize)
    rutagif="./images/panel_2.gif"
    image_to_gif(rutajpgresized,rutagif)

    tortuga = turtle.Turtle(visible=False)
    ventana = turtle.Screen()
    ventana.setup(width=ancho_ventana,height=alto_ventana)
    ventana.bgpic(rutagif)
    ventana.update()

    porcentaje_resize=0.2
    rutajpg="./images/final_up.png"
    rutajpgresized="./images/robot_up.jpg"
    ancho_robot_up,alto_robot_up=resize_jpg(rutajpg,rutajpgresized,porcentaje_resize)
    rutagif="./images/robot_up.gif"
    image_to_gif(rutajpgresized,rutagif)

    porcentaje_resize=0.2
    rutajpg="./images/final_down.png"
    rutajpgresized="./images/robot_down.jpg"
    ancho_robot_down,alto_robot_down=resize_jpg(rutajpg,rutajpgresized,porcentaje_resize)
    rutagif="./images/robot_down.gif"
    image_to_gif(rutajpgresized,rutagif)

    porcentaje_resize=0.2
    rutajpg="./images/final_right.png"
    rutajpgresized="./images/robot_right.jpg"
    ancho_robot_right,alto_robot_right=resize_jpg(rutajpg,rutajpgresized,porcentaje_resize)
    rutagif="./images/robot_right.gif"
    image_to_gif(rutajpgresized,rutagif)

    porcentaje_resize=0.2
    rutajpg="./images/final_left.png"
    rutajpgresized="./images/robot_left.jpg"
    ancho_robot_left,alto_robot_left=resize_jpg(rutajpg,rutajpgresized,porcentaje_resize)
    rutagif="./images/robot_left.gif"
    image_to_gif(rutajpgresized,rutagif)

    
    # ---- Comienza el recorrido de la tortuga ---
    orientacion="up"
    tortuga.penup()
    inicial=[-1/2*ancho_ventana+1/2*ancho_robot_up,-1/2*alto_ventana+1/2*alto_robot_up]
    tortuga.setpos(inicial)
    arriba()
    tortuga.left(90)
    tortuga.showturtle()
    
    print(tortuga.pos())

    #ventana.onclick(tortuga.goto)
    #ventana.onkey(ff, "space")
    #ventana.listen()

    
    puntosSucios=[[52.00,-69.00],[-161.00,7.00],[-117.00,142.00]]
    #for i in range(3):
    #    puntoSucio.append([random.randint(-1/2*ancho_ventana,1/2*ancho_ventana),random.randint(-1/2*alto_ventana,1/2*alto_ventana)])


    # EL RECORRIDO
    retardo=20
    limpia=20
    tortuga.speed(4)
    limpia=False
    c=0
    inter=0
    #time.sleep(30)
    while True:
        limpia=False
        tortuga.forward(50)
        print(orientacion)

        if orientacion == "up":
            for punto in puntosSucios:
                if ((tortuga.pos()[1]+1/2*alto_robot_up>punto[1]) and (tortuga.pos()[1]-1/2*alto_robot_up < punto[1]) and (tortuga.pos()[0]+1/2*ancho_robot_up >punto[0]) and (tortuga.pos()[0]-1/2*ancho_robot_up < punto[0])):
                    # Esta sobre el sucio
                    limpia=True
                    tortuga.speed(0)
                    time.sleep(1)

                else:
                    tortuga.speed(4)


            if ((1/2*alto_ventana-1/2*alto_robot_up)-(tortuga.pos()[1]+1/2*alto_robot_up)<1):
                derecha()
                tortuga.right(90)
                orientacion="right"

        elif orientacion == "right":
            for punto in puntosSucios:
                if ((tortuga.pos()[1]+1/2*alto_robot_right>punto[1]) and (tortuga.pos()[1]-1/2*alto_robot_right < punto[1]) and (tortuga.pos()[0]+1/2*ancho_robot_right>punto[0]) and (tortuga.pos()[0]-1/2*ancho_robot_right < punto[0])):
                    # Esta sobre el sucio
                    limpia=True
                    tortuga.speed(0)
                    time.sleep(1)

                else:
                    tortuga.speed(4)

            
            if c==0:
                posDere=tortuga.pos()
                c+=1 

            if ((posDere[0]+1/2*ancho_robot_right)-(tortuga.pos()[0])<1):
                c=0
                #print(tortuga.pos()[0])
                #tortuga.forward(1/2*ancho_robot_right)
                tortuga.forward(1)
                if (inter % 2) == 0:
                    abajo()
                    tortuga.right(90)
                    orientacion="down"
                    inter+=1
                else:
                    arriba()
                    tortuga.left(90)
                    orientacion="up"
                    inter+=1

            if ((1/2*ancho_ventana-1/2*ancho_robot_right)-(tortuga.pos()[0]+1/2*ancho_robot_right)<1):
                #izquierda()
                orientacion="left"

        elif orientacion == "left":
            for punto in puntosSucios:
                if ((tortuga.pos()[1]+1/2*alto_robot_right>punto[1]) and (tortuga.pos()[1]-1/2*alto_robot_right < punto[1]) and (tortuga.pos()[0]+1/2*ancho_robot_right>punto[0]) and (tortuga.pos()[0]-1/2*ancho_robot_right < punto[0])):
                    # Esta sobre el sucio
                    limpia=True
                    tortuga.speed(0)
                    time.sleep(1)

                else:
                    tortuga.speed(4)
            tortuga.hideturtle()
            orientacion="up"
            tortuga.penup()
            inicial=[-1/2*ancho_ventana+1/2*ancho_robot_up,-1/2*alto_ventana+1/2*alto_robot_up]
            tortuga.setpos(inicial)
            arriba()
            tortuga.left(90)
            tortuga.showturtle()
            c=0
            inter=0
            break

        elif orientacion == "down":
            for punto in puntosSucios:
                if ((tortuga.pos()[1]+1/2*alto_robot_down>punto[1]) and (tortuga.pos()[1]-1/2*alto_robot_down < punto[1]) and (tortuga.pos()[0]+1/2*ancho_robot_down > punto[0]) and (tortuga.pos()[0]-1/2*ancho_robot_down < punto[0])):
                    # Esta sobre el sucio
                    limpia=True
                    tortuga.speed(0)
                    time.sleep(1)

                else:
                    tortuga.speed(4)

            if ((tortuga.pos()[1]-1/2*alto_robot_down)-(-(1/2*alto_ventana-1/4*alto_robot_down))<1):
                derecha()
                tortuga.left(90)
                orientacion="right"

        #tortuga.pos()[0]
        #derecha()
        #tortuga.right(90)
        #ventana.delay(500)



    ventana.mainloop()