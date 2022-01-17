import pyttsx3#Es una biblioteca de conversión de texto a voz en Python. A diferencia de las bibliotecas 
#alternativas, funciona sin conexión y es compatible con Python 2 y 3 
import speech_recognition as sr#es una libreria que nos permite El reconocimiento 
#automático del habla o reconocimiento automático de voz 
import webbrowser#provee una interfaz de alto nivel que permite desplegar documentos 
#basados en la web a los usuarios, y abre el navegador
import datetime#para la fechas y horas
import pywhatkit#me permitira buscar una palabra directamente en el navegador
import pyjokes#libreria que lee bromas de programadores en ingles
import os
import wikipedia#libreria para poder buscar en wikipedia
#escucha nuestro microfono y retorna el audio en texto  using google

def transformar_texto():#funcion para escuchar nuestro microfono, o audio, y  transformalo a texto
    resultado=None#le decimos que q es None, para que cada vez que llamemos la funcion no valga nada
    reconocedor =  sr.Recognizer()#El propósito principal de una instancia de Recognizer es, por supuesto, reconocer el habla. 
    #Cada instancia viene con una variedad de configuraciones y funcionalidades para reconocer el habla de una 
    #fuente de audio
    with sr.Microphone() as fuente:#nosotros vamos a trabajar con nuestro microfono, entonces, con sr.Microphone()
        #le indicamos, y le decimos que lo llamaremos fuente, que es la fuente para lo que mostraremos
        reconocedor.pause_threshold = 0.8#pausar el umbral
        print('yo estoy escuchando')
        said = reconocedor.listen(fuente,3,8, snowboy_configuration=None)#lo que hace la funcion listen es escuchar, entonces
        #le pasamos como primer parametro nuestra fuente, que es la del microfono, el segundo parametro, es el tiempo
        #de espera que le damos al usuario para que comience una frase, antes de darse por vencido, y arroje una excepcion
        #el tercer parametro es el numero maximo de segundos que permite para hablar, para que reconozca la frase, y como
        #cuarto parametro es el snowboy_configuration es un motor de reconocimiento de palabras clave sin conexion, Este 
        #parámetro debe ser None 
        print("resultado:")
        try:
            reconocedor.pause_threshold = 0.8#pausar el umbral
            resultado = reconocedor.recognize_google(said,language = "es",show_all=False)#le decimos que la variable q va a ser igual
            #al reconocimiento de google, entonces utilizamos recognize_google, como primer parametro, le pasamos
            #said, que es la encargada de escuchar lo que le decimos por microfono, como segundo parametro le indicamos
            #el lenguaje, y como tercer parametro le decimos que show_all es false, que es el valor predeterminado,
            #y esto ayuda a devolver la transcripcion mas probable, lo que ha escuchado desde el microfono
            return resultado  #retornamos lo que tiene la variable q, que lo retorne la funcion 
        except sr.UnknownValueError:#excepcion que arroja cuando no escucha nada, o no entiende, en la variable q
            print("perdon, no estoy escuchando")
            return "Estoy Esperando"
        except sr.RequestError:#Excepcion por si no recurso falla
            print('Perdon, el servicio está caido')
            return "Estoy Esperando"
        except:
            return "Estoy Esperando"


#transform()


#---------------FUNCION PARA HACER HABLAR LA COMPUTADORA----------------------------    
def Hablar(mensaje):#le pasamos por parametro el mensaje que dirá el asistente de voz
    voz = pyttsx3.init()#utilizamos la libreria pyttsx3, que para convertir de texto a voz, y con la funcion init()
    #le estamos diciendo que ahora la variable voz, tendra todo lo que hace la libreria
    voz.say(mensaje)#ahora que voz, tiene todo lo de la libreria, utilizamos la funcion 'say' que es para que la voz
    #se ejecute, say en ingles es "decir", y le pasamos como parametro, el parametro que nos pasan a la funcion
    voz.runAndWait()#ejecutamos la variable voz

#----------------------------------------------------
voz = pyttsx3.init()#volvemos a utilizar y decirle que la variable voz, podra hacer todo lo de la libreria, esta variable
#ya es diferente a la del metodo "hablar", por eso toca volverle a decir 

#for voice in voz.getProperty('voices'):#esto for es para mirar las voces que tenemos en nuestros computador, con la funcion
    #getProperty('voices')
 #  print(voice)#las mostramos


id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'#sera la voz utilizada
voz.setProperty('voice',id)#le agregamos la propieda, en 'voice', lo que le estamos diciendo es que utilizamos la voz
#que hemos almacenado en la variable id
voz.runAndWait()#ejecutamos la variable

#---------retorna el dia de la semana-----------
def Consulta_dia():
    dia = datetime.date.today()#declaramos la variable y utilizamos la libreria importada datetime, utilizamos
    #la clase date, que es para la fecha, y despues utilizamos la funcion today() que nos retorna el dia de hoy
    print(dia)
    weekday = dia.weekday()#la funcion weekday retorna el dia de la semana, donde lunes es = 0, martes = 1, etc
    print(weekday)
    Mapping = {#hacemos un mapeo, que es una función incorporada que le permite procesar y transformar 
    #todos los elementos en un iterable sin usar un bucle for 
        0: 'Lunes',
        1:'Martes',
        2: 'Miercoles',
        3:'Jueves',
        4: 'Viernes',
        5: 'Sabado',
        6: 'Domingo'
    }
    try:
        Hablar(f'el dia de hoy es el {Mapping[weekday]}')#llamamos a la funcion hablar, que es la encargada de 
        #hablarnos a traves de la voz del computador, y en el parametro le pasamos la funcion mapping[weekday] y le 
        #decimos que transforme los numeros que retorna weekday, en lunes o martes o miercoles etc. recordar que
        #la funcion weekday retorna el dia de la semana, donde lunes es = 0, martes = 1, etc
    except:
        pass
#--------------------------------------

#retorna el tiempo
def consulta_tiempo():
    tiempo = datetime.datetime.now().strftime("%I:%M:%S")#utilizamos la libreria datetime,y le indicamos que nos
    #diga la fecha del momento, y con strftime() devuelve la fecha y hora representado en cadena, en texto
    Hablar(f"la hora es: {tiempo[0:2]} y {tiempo[3:5]} minutos")


#--------------------------------------
#un saludo al inicio
def saludo():
    Hablar("Hola, mi nombre es Helena, yo soy tu asistente personal. Como puedo Ayudarte")#llamamos al funcion hablar
    #que es la encargada de hablar, y le pasamos en el parametro lo que queremos que diga

#------------------------------------

#El nucleo de nuestro asistente, acepta consulta, y devuelve respuestas

def inicio():
    saludo()#llamamos la funcion saludo, para iniciar nuestro programa
    while(True):
        
        q = transformar_texto().lower()#decimos que la variable
        print(q)
        if 'comenzar youtube' in q:#funciona
            Hablar("Iniciando Youtube para ti. Espera un segundo.")
            webbrowser.open('https://www.youtube.com')#con la libreria webbbrowser, y con la funcion abrimos youtube,
            #le pasamos la url
            continue
        elif 'comenzar navegador' in q:#funciona
            Hablar('Abriendo Navegador')
            webbrowser.open('https//www.google.com')#con la libreria webbbrowser, y con la funcion abrimos youtube,
            #le pasamos la url
            continue
        elif 'qué día es hoy' in q:#funciona
            Consulta_dia()#llamamos la funcion consulta_dia que es la encargada de devolvernos que dia es hoy
            continue
        elif 'hora' in q:#funciona
            consulta_tiempo()#llamamos la funcion consulta_tiempo que es la encargada de devolvernos la hora actual
            continue
        elif 'adiós' in q:#funciona
            Hablar('OK, nos vemos luego')#llamamos la funcion hablar, y que nos diga lo que le pasamos por parametro
            break

        elif 'tu nombre' in q:#funciona
            Hablar("Yo soy helena. Tu asistente de audio")#llamamos a la funcion hablar, y le indicamos en el parametro
            #los que debe decir
            continue
        elif 'buscar en web' in q:#funciona
            Hablar("que desea buscar?")
            busqueda = transformar_texto().lower()#creamos una nueva variable, y volvemos a llamar la funcion transformar_texto.lower()
            #lower es para que nos devuelva en texto, y ahí decimos lo que queremos buscar
            print(busqueda)
            pywhatkit.search(busqueda)#utilizamos la libreria, que nos ayuda a buscar directamente en nuestro
            #navegador, y le decimos con la funcion search(busqueda) que busque lo que hemos hablado
            Hablar("Esto es lo que encuentro")
            continue
        elif 'jugar' in q:#funciona
            Hablar(f'La opción escogida es {q}')#hacemos hablar al asistente
            pywhatkit.playonyt(q)#con la funcion playonyt, nos abre algun video en youtube, play-on-yt, abrir en 
            #youtube, y abrimos q, que es "jugar"
            continue
        elif 'broma' in q:#funciona
            Hablar(pyjokes.get_joke())#utilizamos la libreria pyjokes, que es para chistes de programadores, en ingles
            #y con la funcion get_joke, le decimos que nos muestre los chistes que tiene
            continue
        

inicio()

