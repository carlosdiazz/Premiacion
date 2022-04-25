Loto_LA_SUERTE_Pages= 'https://lasuertedominicana.com/app/index.php/front/index'
Loto_LA_SUERTE_Resulado = 'https://lasuertedominicana.com/app/index.php/front/index'
Loto_LA_SUERTE_Fecha= '/html/body/div[2]/div[3]/main/div/div[2]/div/p'
Loto_LA_SUERTE_Numbers_1 = '/html/body/div[2]/div[3]/main/div/div[2]/div/div/div[1]/span'
Loto_LA_SUERTE_Numbers_2 = '/html/body/div[2]/div[3]/main/div/div[2]/div/div/div[2]/span'
Loto_LA_SUERTE_Numbers_3 = '/html/body/div[2]/div[3]/main/div/div[2]/div/div/div[3]/span'

#! ESTE BUTTON FUNCIONA QUE AL INICIAR LA PAGINA HAY QUE CERRAR UN CUADRO
LOTO_BUTTON_CERRAR = '/html/body/div[2]/div/div[1]/div/button'


La_suerte_Todo = {
    'URL' : [Loto_LA_SUERTE_Pages, Loto_LA_SUERTE_Pages,LOTO_BUTTON_CERRAR ],
    'FECHA' : [Loto_LA_SUERTE_Fecha ],
    'NUMEROS' : [Loto_LA_SUERTE_Numbers_1, Loto_LA_SUERTE_Numbers_2, Loto_LA_SUERTE_Numbers_3 ]
}
#?Significa QUE ES Dominicana SI ES False
LOTTERY_LA_SUERTE_TODO = [La_suerte_Todo,La_suerte_Todo, False]