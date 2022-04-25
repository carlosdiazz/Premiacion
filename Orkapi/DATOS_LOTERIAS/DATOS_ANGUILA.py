Anguila_Pages = 'https://anguillalottery.ai/'
Anguila_Fecha_SOrteo = '/html/body/div[4]/div/div[2]/div[1]/div[1]/div'
Anguila_Number1 = '/html/body/div[4]/div/div[2]/div[1]/div[2]/span[1]'
Anguila_Number2 = '/html/body/div[4]/div/div[2]/div[1]/div[2]/span[2]'
Anguila_Number3 = '/html/body/div[4]/div/div[2]/div[1]/div[2]/span[3]'

ANGUILA_TODO = {
    'URL' : [Anguila_Pages, Anguila_Pages],
    'FECHA' : [Anguila_Fecha_SOrteo ],
    'NUMEROS' : [Anguila_Number1, Anguila_Number2, Anguila_Number3 ]
}
#?Significa QUE ES Dominicana SI ES False
ANGUILA_LOTTERY_TODO = [ANGUILA_TODO,ANGUILA_TODO, False]