NY_LOTTERY = 'https://www.nylottery.org/'
NY_LOTETERY_NUMBERS = 'https://www.nylottery.org/numbers/evening'
NY_LOTTERY_WIND4 = 'https://www.nylottery.org/win-4/evening'

NY_LOTTERY_NUMBERS_fecha = '/html/body/div/div/table/tbody/tr[2]/td[1]/a'
NY_LOTTERY_NUMBERS_NU1 = '/html/body/div/div/table/tbody/tr[2]/td[2]/span[2]'
NY_LOTTERY_NUMBERS_NU2 = '/html/body/div/div/table/tbody/tr[2]/td[2]/span[3]'

NY_LOTTERY_WIND4_fecha ='/html/body/div/div/table/tbody/tr[2]/td[1]/a'
NY_LOTTERY_WIND4_NU3 = '/html/body/div/div/table/tbody/tr[2]/td[2]/span[1]'
NY_LOTTERY_WIND4_NU4 = '/html/body/div/div/table/tbody/tr[2]/td[2]/span[2]'
NY_LOTTERY_WIND4_NU5 = '/html/body/div/div/table/tbody/tr[2]/td[2]/span[3]'
NY_LOTTERY_WIND4_NU6 = '/html/body/div/div/table/tbody/tr[2]/td[2]/span[4]'

NEW_YORK_LOTTERY = {
    'URL'     : [NY_LOTTERY, NY_LOTETERY_NUMBERS,NY_LOTTERY_WIND4],
    "TRES"    : [NY_LOTTERY_NUMBERS_fecha, NY_LOTTERY_NUMBERS_NU1, NY_LOTTERY_NUMBERS_NU2],
    "CUATRO"  : [NY_LOTTERY_WIND4_fecha,NY_LOTTERY_WIND4_NU3,NY_LOTTERY_WIND4_NU4,NY_LOTTERY_WIND4_NU5,NY_LOTTERY_WIND4_NU6]
}
#! --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

NY_LOTTERYUSA = 'https://www.lotteryusa.com/'
NY_LOTTERYUSA_NUMBERS = 'https://www.lotteryusa.com/new-york/numbers/'
NY_LOTTERYUSA_WIND4 = 'https://www.lotteryusa.com/new-york/win-4/'

NY_LOTTERYUSA_Numbers_FECHA = '//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time'
NY_LOTTERYUSA_Numbers_NU1 = '//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span'
NY_LOTTERYUSA_Numbers_NU2 = '//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[3]/span'

NY_LOTTERYUSA_WIND4_FECHA = '//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time'
NY_LOTTERYUSA_WIND4_NU3 = '//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[1]/span'
NY_LOTTERYUSA_WIND4_NU4 = '//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span'
NY_LOTTERYUSA_WIND4_NU5 = '//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[3]/span'
NY_LOTTERYUSA_WIND4_NU6 = '//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[4]/span'

NEW_YORK_LOTTERYUSA = {
    'URL' : [NY_LOTTERYUSA, NY_LOTTERYUSA_NUMBERS, NY_LOTTERYUSA_WIND4],
    'TRES' : [NY_LOTTERYUSA_Numbers_FECHA,NY_LOTTERYUSA_Numbers_NU1,NY_LOTTERYUSA_Numbers_NU2 ],
    'CUATRO' : [NY_LOTTERYUSA_WIND4_FECHA,NY_LOTTERYUSA_WIND4_NU3,NY_LOTTERYUSA_WIND4_NU4,NY_LOTTERYUSA_WIND4_NU5,NY_LOTTERYUSA_WIND4_NU6 ]
}
#! --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

NEW_YORk_OFICIAL_pages = 'https://nylottery.ny.gov/'
NEW_YORk_OFICIAL_Numbers = 'https://nylottery.ny.gov/draw-game?game=numbers'
NEW_YORk_OFICIAL_WIN4 = 'https://nylottery.ny.gov/draw-game?game=win4'

NEW_YORK_OFICIAL_Numbers_Fecha = '/html/body/div/div[1]/div[4]/main/div/div[1]/div[1]/div[2]/div/div[1]/div[1]/p/span'
NEW_YORK_OFICIAL_Numbers_Nu1 = '/html/body/div/div[1]/div[4]/main/div/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/div/div[2]'
NEW_YORK_OFICIAL_Numbers_Nu2 = '/html/body/div/div[1]/div[4]/main/div/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/div/div[3]'

NEW_YORK_OFICIAL_WIN_Fecha = '/html/body/div/div[1]/div[4]/main/div/div[1]/div[1]/div[2]/div/div[1]/div[1]/p/span'
NEW_YORK_OFICIAL_WIN_Nu3 = '/html/body/div/div[1]/div[4]/main/div/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/div/div[1]'
NEW_YORK_OFICIAL_WIN_Nu4 = '/html/body/div/div[1]/div[4]/main/div/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/div/div[2]'
NEW_YORK_OFICIAL_WIN_Nu5 = '/html/body/div/div[1]/div[4]/main/div/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/div/div[3]'
NEW_YORK_OFICIAL_WIN_Nu6 = '/html/body/div/div[1]/div[4]/main/div/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/div/div[4]'


NEW_YORk_OFICIAL = {
    'URL': [NEW_YORk_OFICIAL_pages, NEW_YORk_OFICIAL_Numbers, NEW_YORk_OFICIAL_WIN4],
    'TRES' : [NEW_YORK_OFICIAL_Numbers_Fecha, NEW_YORK_OFICIAL_Numbers_Nu1, NEW_YORK_OFICIAL_Numbers_Nu2  ],
    'CUATRO' : [NEW_YORK_OFICIAL_WIN_Fecha, NEW_YORK_OFICIAL_WIN_Nu3, NEW_YORK_OFICIAL_WIN_Nu4, NEW_YORK_OFICIAL_WIN_Nu5, NEW_YORK_OFICIAL_WIN_Nu6  ]
}

#! --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#?Significa QUE ES AMERICANA SI ES TRUE
NEW_TORK_NOCHE_TODO = [NEW_YORK_LOTTERY, NEW_YORK_LOTTERYUSA, True]
