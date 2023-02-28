#Prueba tecnica Efrain Blanco   
#########################################################################################################
#Solicitar nombres de jugadores

#Validar que usuario escriba un nombre jugador 1
a=0
while a!=1:
  jugador1=input("Escribe el nombre del jugador 1: ")
  
  if jugador1 =="":
    print(" Escribe un nombre por favor")

  else:
    a=1
  
  
#Validar que usuario escriba un nombre jugador 2
b=0
while b!=1:
  jugador2=input("Escribe el nombre del jugador 2: ")
  
  if jugador2 =="":
    print(" Escribe un nombre por favor")

  else:
    b=1



#################################################################################

#Preguntar si inicia juego
iniciar=input("¿Deseas iniciar el juego?: ").lower()

############################################################################################
#Iniciando variables
puntaje_jugador1=0
puntaje_jugador2=0

juegos_ganados1=0
juegos_ganados2=0

marcador_jugador1=0
marcador_jugador2=0

ventaja1=0
ventaja2=0

aux2=0
auxb=0
auxc=0
auxd=0
auxe=0
terminado="no"
##############################################################################################


#if 1
if iniciar=="si":
  print("codigo de if 1")

  #while 1 (de terminar juego en caso de ganador)
  while terminado!="si":
    #Mostrar en pantalla nombre de jugadores
    print("El nombre del jugador #1 es: ",jugador1)
    print("El nombre del jugador #2 es: ",jugador2)
    print(" ")
    #Mostrar marcador iniciando jugador 2
    print("El marcador inicial del juego actual del jugador #1", jugador1, " es: ", marcador_jugador1, " puntos")
    print("El marcador inicial glogal de juegos ganados de jugador #1", jugador1, " es: ", juegos_ganados1)
    print(" ")
    #Mostrar marcador iniciando jugador 2
    print("El marcador inicial del juego actual del jugador #2", jugador2, " es: ", marcador_jugador2, " puntos")
    print("El marcador inicial glogal de juegos ganados de jugador #2", jugador2, " es: ", juegos_ganados2)
    print(" ")
    #Pedir puntajes 

    #while 2 (de pedir puntajes)
    while aux2!=1:
      #while 3 (de pedir nombre del jugador que gana punto)
      while auxb!=1:
        puntaje=input("Escribe el nombre del jugador ganador del punto actual: ").lower()
        #if 2
        if puntaje==jugador1:
          puntaje_jugador1+=1
          #JUGADOR 1 SUMA DE PUNTOS
          
          #if 3
          if puntaje_jugador1==1: #15 puntos
            marcador_jugador1=15
            auxb=1
            print("codigo if 3")
          elif puntaje_jugador1==2: #30 puntos
            marcador_jugador1=marcador_jugador1+15
            auxb=1
            print("codigo if 3")
          elif puntaje_jugador1==3: #40 puntos
            marcador_jugador1=marcador_jugador1+10
            auxb=1

            
          #ganar juego sin empates ni ventajas
          if marcador_jugador1==50 and marcador_jugador2<40:
            juegos_ganados1+=1
            auxb=1
            

          #Mostrar marcador ganando jugador 1
          print("El marcador del juego actual del jugador #1", jugador1, " es: ", marcador_jugador1, " puntos")
          print("El marcador glogal de juegos ganados de jugador #1", jugador1, " es: ", juegos_ganados1)
          #Mostrar marcador ganando jugador 2
          print("El marcador del juego actual del jugador #2", jugador2, " es: ", marcador_jugador2, " puntos")
          print("El marcador glogal de juegos ganados de jugador #2", jugador2, " es: ", juegos_ganados2)     

      ####################################################################    
          #if 5 (De empate y ventajas)
          if puntaje_jugador1==4 and marcador_jugador2==40:
            ventaja1+=1
            auxb=1
            if ventaja2==1:
              ventaja1=0
              puntaje_jugador1=3
              auxb=1

            
            ##print("codigo if 5")
            
            ##print("codifo if 6")

           
          if (puntaje_jugador1-puntaje_jugador2)==2:
            juegos_ganados1+=1
            aux2=1
            auxb=1
########################################################################
            
          #if 4 (ganador jugador 1)
          if juegos_ganados1==7:
            auxb=1
            aux2=1
            terminado="si"
            print("¡El ganador del juego es ",jugador1,"! con 7 juegos ganados (1set)")
            print("El jugador #2 ",jugador2, " quedó con ",juegos_ganados2, " juegos ganados")
            print("codigo if 4")
            
          ##print("codigo if 2")
          
        elif puntaje==jugador2:
          puntaje_jugador2+=1
          #JUGADOR 2 SUMA DE PUNTOS
          
          #if 3
          if puntaje_jugador2==1: #15 puntos
            marcador_jugador2=15
            print("codigo if 3")
          elif puntaje_jugador2==2: #30 puntos
            marcador_jugador2=marcador_jugador2+15
            print("codigo if 3")
          elif puntaje_jugador2==3: #40 puntos
            marcador_jugador2=marcador_jugador2+10

            
          #ganar juego sin empates ni ventajas
          if marcador_jugador2==50 and marcador_jugador1<40:
            juegos_ganados2+=1
            aux2=1
            

          #Mostrar marcador ganando jugador 1
          print("El marcador del juego actual del jugador #1", jugador1, " es: ", marcador_jugador1, " puntos")
          print("El marcador global de juegos ganados de jugador #1", jugador1, " es: ", juegos_ganados1)
          #Mostrar marcador ganando jugador 2
          print("El marcador del juego actual del jugador #2", jugador2, " es: ", marcador_jugador2, " puntos")
          print("El marcador global de juegos ganados de jugador #2", jugador2, " es: ", juegos_ganados2)     

      ####################################################################    
          #if 5 (De empate y ventajas)
          if puntaje_jugador2==4 and marcador_jugador1==40:
            ventaja2+=1
            if ventaja1==1:
              ventaja2=0
              puntaje_jugador2=3

            
            ##print("codigo if 5")
          #if 6  
          if puntaje_jugador2==5 and marcador_jugador1==40:
            ventaja2+=1
            juegos_ganados2+=1
            aux2=1
            
            ##print("codifo if 6")

           
          if (puntaje_jugador2-puntaje_jugador1)==2:
            juegos_ganados2+=1
            aux2=1
########################################################################
            
          #if 4 (ganador jugador 2)
          if juegos_ganados2==7:
            terminado="si"
            print("¡El ganador del juego es ",jugador2,"! con 7 juegos ganados (1set)")
            print("El jugador #2 ",jugador1, " quedó con ",juegos_ganados1, " juegos ganados")
            print("codigo if 4")
            
          ##print("codigo if 2")


          
          ##print("codigo if 2")
          auxb=1
        else:
          print(puntaje, " no es correcto, escribe por favor ",jugador1, " o", jugador2)


        auxb=1 
        ##print("codigo while 3")
      
      ##print("codigo de while 2")

     
    ##print("codigo de while 1")
    #####
  
#else de if 1
else:
  print("El juego no fue iniciado")