Loto_La_Primera_AM_Pages= 'https://laprimera.do/'
Loto_La_Primera_AM_Resulado = 'https://laprimera.do/'
Loto_La_Primera_AM_Fecha= '/html/body/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[2]/strong'
Loto_La_Primera_AM_Numbers_1 = '/html/body/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div[1]/div[2]/div[1]/span'
Loto_La_Primera_AM_Numbers_2 = '/html/body/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/span'
Loto_La_Primera_AM_Numbers_3 = '/html/body/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div[1]/div[2]/div[3]/span'


La_Primera_AM_Todo = {
    'URL' : [Loto_La_Primera_AM_Pages, Loto_La_Primera_AM_Resulado],
    'FECHA' : [Loto_La_Primera_AM_Fecha ],
    'NUMEROS' : [Loto_La_Primera_AM_Numbers_1, Loto_La_Primera_AM_Numbers_2, Loto_La_Primera_AM_Numbers_3 ]
}
#?Significa QUE ES Dominicana SI ES False
LOTTERY_LA_PRIMERA_AM = [La_Primera_AM_Todo,La_Primera_AM_Todo, False]