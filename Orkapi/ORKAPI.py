from ColocarPremio import Colocar_Numeros_Plataforma

url = 'https://dev_admin.orkapi.net/'
username = 'carlos@premio'
password = 1234

def ORKAPI(loteria, horario, numeros_a_publicar):

    print("Los numeros han sido confirmados y son Correctos")
    print("Los numeros que se van a publicar son")
    print(numeros_a_publicar)

    comprobar=Colocar_Numeros_Plataforma(url, username, password, loteria,horario, numeros_a_publicar).Resultadoo()
    if(comprobar == True):
        print('Numero Publicadon Correctamente')
        numero_1 = numeros_a_publicar[0]
        numero_2 = numeros_a_publicar[1]
        numero_3 = numeros_a_publicar[2]
        return [True,f'Numero Publicado Correctamente \nPara la Loteria: {loteria}\nCon el horario: {horario} \nLos numeros son: {numero_1}-{numero_2}-{numero_3}']
    else:
        print(comprobar)
        return [False,comprobar]