URL_PLTAFORMA = 'https://dev_admin.orkapi.net/login/'
URL_PREMIOS = 'https://dev_admin.orkapi.net/operaciones/premios/'
Input_User= '//*[@id="usuario_username"]'
Input_Password = '//*[@id="usuario_password"]'
boton_Login = '//*[@id="new_usuario"]/div[4]/div[2]/input'
Input_Loteria = '/html/body/div[2]/div/div/div/div[2]/div[1]/div[2]/div/table/thead/tr[2]/th[1]/div/input'
Input_Sorteo = '/html/body/div[2]/div/div/div/div[2]/div[1]/div[2]/div/table/thead/tr[2]/th[4]/div/input'
Seleccionar_Loteria = '/html/body/div[2]/div/div/div/div[2]/div[1]/div[2]/div/table/tbody/tr[1]/td[1]'
Premio_1 = '/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/form/div[1]/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[2]/div/input'
Premio_2 = '/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/form/div[1]/div/div/div/div/div[2]/div/table/tbody/tr[2]/td[2]/div/input'
Premio_3 = '/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/form/div[1]/div/div/div/div/div[2]/div/table/tbody/tr[3]/td[2]/div/input'
Boton_Premiar = '/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/form/div[2]/div/button[2]'

PLATAFORMA_TODO = [
    URL_PLTAFORMA,
    URL_PREMIOS,
    Input_User,
    Input_Password,
    boton_Login,
    Input_Loteria,
    Input_Sorteo,
    Seleccionar_Loteria,
    Premio_1,
    Premio_2,
    Premio_3,
    Boton_Premiar
]