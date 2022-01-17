import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pywhatkit
import pyjokes
import os


def transformar_texto():
    resultado=None
    reconocedor =  sr.Recognizer()
    with sr.Microphone() as fuente:
        reconocedor.pause_threshold = 0.8
        print('yo estoy escuchando')
        said = reconocedor.listen(fuente,3,6, snowboy_configuration=None)
        print("resultado:")
        try:
            reconocedor.pause_threshold = 0.8
            resultado = reconocedor.recognize_google(said,language = "es",show_all=False)
            return resultado  
        except sr.UnknownValueError:
            print("perdon, no estoy escuchando")
            return "Estoy Esperando"
        except sr.RequestError:
            print('Perdon, el servicio está caido')
            return "Estoy Esperando"
        except:
            return "Estoy Esperando"





#---------------FUNCION PARA HACER HABLAR LA COMPUTADORA----------------------------  
#   
def Hablar(mensaje):
    voz = pyttsx3.init()
    voz.say(mensaje)
    voz.runAndWait()

#----------------------------------------------------
voz = pyttsx3.init()

#for voice in voz.getProperty('voices'):
    #getProperty('voices')
 #  print(voice)#las mostramos


id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
voz.setProperty('voice',id)
voz.runAndWait()

#---------retorna el dia de la semana-----------
def Consulta_dia():
    dia = datetime.date.today()
    print(dia)
    weekday = dia.weekday()
    print(weekday)
    Mapping = {
        0: 'Lunes',
        1:'Martes',
        2: 'Miercoles',
        3:'Jueves',
        4: 'Viernes',
        5: 'Sabado',
        6: 'Domingo'
    }
    try:
        Hablar(f'el dia de hoy es el {Mapping[weekday]}')
    except:
        pass
#--------------------------------------

#retorna el tiempo
def consulta_tiempo():
    tiempo = datetime.datetime.now().strftime("%I:%M:%S")
    Hablar(f"la hora es: {tiempo[0:2]} y {tiempo[3:5]} minutos")


#--------------------------------------
#un saludo al inicio
def saludo():
    Hablar("Hola, mi nombre es Helena, yo soy tu asistente personal. Como puedo Ayudarte")

#------------------------------------

#El nucleo de nuestro asistente, acepta consulta, y devuelve respuestas

def inicio():
    saludo()
    while(True):
        
        q = transformar_texto().lower()
        print(q)
        if 'comenzar youtube' in q:
            Hablar("Iniciando Youtube para ti. Espera un segundo.")
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'comenzar navegador' in q:
            Hablar('Abriendo Navegador')
            webbrowser.open('https//www.google.com')
            continue
        elif 'qué día es hoy' in q:
            Consulta_dia()
            continue
        elif 'hora' in q:
            consulta_tiempo()
            continue
        elif 'adiós' in q:
            Hablar('OK, nos vemos luego')
            break

        elif 'tu nombre' in q:
            Hablar("Yo soy helena. Tu asistente de audio")
            continue
        elif 'buscar en web' in q:
            Hablar("que desea buscar?")
            busqueda = transformar_texto().lower()
            print(busqueda)
            pywhatkit.search(busqueda)
            Hablar("Esto es lo que encuentro")
            continue
        elif 'jugar' in q:
            Hablar(f'La opción escogida es {q}')
            continue
        elif 'broma' in q:
            Hablar(pyjokes.get_joke())
            continue
        else: 
            print('Perdon, no tengo datos para esto')
inicio()