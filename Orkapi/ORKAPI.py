from ColocarPremio import Colocar_Numeros_Plataforma

#url = 'https://dev_admin.orkapi.net/'
#username = 'carlos@premio'
#password = 1234

#! Con esta funcion entro a la cuenta de Orkapi para poder publicar los numneros

def ORKAPI(loteria, horario, numeros_a_publicar,url,username,password):

    print("\n\nLos numeros han sido confirmados y son Correctos\n\n")
    print("\n\nLos numeros que se van a publicar son\n\n")
    print(f"---------------> {numeros_a_publicar}\n\n")

    comprobar=Colocar_Numeros_Plataforma(url, username, password, loteria,horario, numeros_a_publicar).Resultadoo()
    if(comprobar == True):
        print('\n\nNumero Publicadon Correctamente\n\n')
        numero_1 = numeros_a_publicar[0]
        numero_2 = numeros_a_publicar[1]
        numero_3 = numeros_a_publicar[2]
        return [True,f'Numero Publicado Correctamente \nPara la Loteria: {loteria}\nCon el horario: {horario} \nLos numeros son: {numero_1}-{numero_2}-{numero_3}']
    else:
        print(comprobar)
        return [False,comprobar]