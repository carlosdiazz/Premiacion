Loto_Ganamas_Pages= 'https://loterianacional.gob.do/index.php'
Loto_Ganamas_Resulado = 'https://loterianacional.gob.do/index.php'
Loto_Ganamas_Fecha= '/html/body/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/table[2]/tbody/tr[1]/td[2]/span'
Loto_Ganamas_Numbers_1 = '/html/body/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/table[2]/tbody/tr[2]/td[1]/span'
Loto_Ganamas_Numbers_2 = '/html/body/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/table[2]/tbody/tr[2]/td[2]/span'
Loto_Ganamas_Numbers_3 = '/html/body/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/table[2]/tbody/tr[2]/td[3]/span'


Ganamas_Todo = {
    'URL' : [Loto_Ganamas_Pages, Loto_Ganamas_Resulado],
    'FECHA' : [Loto_Ganamas_Fecha ],
    'NUMEROS' : [Loto_Ganamas_Numbers_1, Loto_Ganamas_Numbers_2, Loto_Ganamas_Numbers_3 ]
}
#?Significa QUE ES Dominicana SI ES False
LOTTERY_GANAMAS_TODO = [Ganamas_Todo,Ganamas_Todo, False]