Loto_La_Primera_PM_Pages= 'https://laprimera.do/'
Loto_La_Primera_PM_Resulado = 'https://laprimera.do/'
Loto_La_Primera_PM_Fecha= '/html/body/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[2]/strong'
Loto_La_Primera_PM_Numbers_1 = '/html/body/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div[2]/div[2]/div[1]/span'
Loto_La_Primera_PM_Numbers_2 = '/html/body/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div[2]/div[2]/div[2]/span'
Loto_La_Primera_PM_Numbers_3 = '/html/body/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div[2]/div[2]/div[3]/span'

La_Primera_PM_Todo = {
    'URL' : [Loto_La_Primera_PM_Pages, Loto_La_Primera_PM_Resulado],
    'FECHA' : [Loto_La_Primera_PM_Fecha ],
    'NUMEROS' : [Loto_La_Primera_PM_Numbers_1, Loto_La_Primera_PM_Numbers_2, Loto_La_Primera_PM_Numbers_3 ]
}
#?Significa QUE ES Dominicana SI ES False
LOTTERY_LA_PRIMERA_PM = [La_Primera_PM_Todo,La_Primera_PM_Todo, False]