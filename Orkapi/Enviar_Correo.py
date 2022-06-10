# Importamos librerías
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from TOKEN_API_PRO_DE import CORREO, PASS_CORREO
from Funciones_Necesarias import fecha

#! Con esta funcion envio un correo con los nuemros que se mandan a gaurdar a base de datos, por el momento solo se envia al correo personal mio

def Enviar_Corre(loteria_Datos):
    try:
        print(f'\n\nEnviando Correo\n\n')
        loteria = loteria_Datos[0]
        sorteo = loteria_Datos[1]
        numeros_ganadores = loteria_Datos[2]
        numero_1= numeros_ganadores[0]
        numero_2= numeros_ganadores[1]
        numero_3= numeros_ganadores[2]
        fecha_hoy = loteria_Datos[3]
        agregado_por = loteria_Datos[4]

        # Creamos objeto Multipart, quien será el recipiente que enviaremos
        msg = MIMEMultipart()
        msg['From']="CORREO"
        msg['To']="c.diazadriann@gmail.com"
        msg['Subject']=f"Numeros de la loteria {loteria} del sorteo: {sorteo} "
        msg['']

        #Mensaje
        mensaje = f'Loteria: {loteria} ,Sorteo {sorteo} Los numeros son {numero_1}-{numero_2}-{numero_3} en la fecha de {fecha_hoy}, agregado por: {agregado_por}'
        msg.attach(MIMEText(mensaje, 'plain'))


        # Adjuntamos Imagen
        file = open("./LOTERIA_PAGES.png", "rb")
        attach_image = MIMEImage(file.read())
        msg.attach(attach_image)

        # Autenticamos
        mailServer = smtplib.SMTP('smtp.gmail.com',587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(CORREO,PASS_CORREO)

        # Enviamos
        mailServer.sendmail(CORREO, "c.diazadriann@gmail.com", msg.as_string())

        # Cerramos conexión
        mailServer.close()
        print(f'\nCorreo Enviado Correctacmente\n')
    except:
        print("\n\nNo se pudo Enviar el correo\n\n")
        #return('No se pudo Enviar el correo')