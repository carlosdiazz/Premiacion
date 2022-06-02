Loto_Leidsa_Pages= 'https://www.leidsa.com/'
Loto_Leidsa_Resulado = 'https://www.leidsa.com/'
Loto_Leidsa_Fecha= '/html/body/div/section[2]/div/div[3]/div[3]/div/div[1]/p'
Loto_Leidsa_Numbers_1 = '/html/body/div/section[2]/div/div[3]/div[3]/div/div[2]/table/tbody/tr[1]/td'
Loto_Leidsa_Numbers_2 = '/html/body/div/section[2]/div/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td'
Loto_Leidsa_Numbers_3 = '/html/body/div/section[2]/div/div[3]/div[3]/div/div[2]/table/tbody/tr[3]/td'

BOTON_CERRAR = '/html/body/div[2]/div/div[1]/div/button'

Leidsa_Todo = {
    'URL' : [Loto_Leidsa_Pages, Loto_Leidsa_Resulado],
    'FECHA' : [Loto_Leidsa_Fecha ],
    'NUMEROS' : [Loto_Leidsa_Numbers_1, Loto_Leidsa_Numbers_2, Loto_Leidsa_Numbers_3 ]
}
#?Significa QUE ES Dominicana SI ES False
LOTTERY_LEIDSA_TODO = [Leidsa_Todo,Leidsa_Todo, False]