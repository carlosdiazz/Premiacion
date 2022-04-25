Loto_Nacional_Pages= 'https://loterianacional.gob.do/index.php'
Loto_Nacional_Resulado = 'https://loterianacional.gob.do/index.php'
Loto_Nacional_Fecha= '/html/body/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/table[3]/tbody/tr[1]/td[2]/span'
Loto_Nacional_Numbers_1 = '/html/body/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/table[3]/tbody/tr[2]/td[1]/span'
Loto_Nacional_Numbers_2 = '/html/body/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/table[3]/tbody/tr[2]/td[2]/span'
Loto_Nacional_Numbers_3 = '/html/body/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/table[3]/tbody/tr[2]/td[3]/span'


Nacional_Todo = {
    'URL' : [Loto_Nacional_Pages, Loto_Nacional_Pages ],
    'FECHA' : [Loto_Nacional_Fecha ],
    'NUMEROS' : [Loto_Nacional_Numbers_1, Loto_Nacional_Numbers_2, Loto_Nacional_Numbers_3 ]
}
#?Significa QUE ES Dominicana SI ES False
LOTTERY_NACIONAL_TODO = [Nacional_Todo,Nacional_Todo, False]