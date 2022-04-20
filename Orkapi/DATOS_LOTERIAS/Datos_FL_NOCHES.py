FL_LO_USA_PAGES = 'https://www.lotteryusa.com/'
FL_LO_USA_NUMBERS = 'https://www.lotteryusa.com/florida/pick-3/'
FL_LO_USA_WIND4 = 'https://www.lotteryusa.com/florida/pick-4/'

FL_LO_NUMBERS_fecha = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time'
FL_LO_NUMBERS_NU1 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span'
FL_LO_NUMBERS_NU2 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[3]/span'

NY_LOTTERY_WIND4_fecha ='/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time'
NY_LOTTERY_WIND4_NU3 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[1]/span'
NY_LOTTERY_WIND4_NU4 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span'
NY_LOTTERY_WIND4_NU5 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[3]/span'
NY_LOTTERY_WIND4_NU6 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[4]/span'

FLORIDA_LOTTERY_USA_NOCHE = {
    'URL'     : [FL_LO_USA_PAGES,FL_LO_USA_NUMBERS,FL_LO_USA_WIND4],
    "TRES"    : [FL_LO_NUMBERS_fecha,FL_LO_NUMBERS_NU1,FL_LO_NUMBERS_NU2 ],
    "CUATRO"  : [NY_LOTTERY_WIND4_fecha,NY_LOTTERY_WIND4_NU3,NY_LOTTERY_WIND4_NU4,NY_LOTTERY_WIND4_NU5,NY_LOTTERY_WIND4_NU6]
}
#! --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

FL_OFI_PAGES_NOCHE = 'https://www.flalottery.com/'
FL_OFI_NUMBERS_NOCHE = 'https://www.flalottery.com/pick3'
FL_OFI_WIND4_NOCHE = 'https://www.flalottery.com/pick4'

FL_OFI_NUMBERS_FECHA_NOCHE = '/html/body/div[3]/div[3]/section[2]/div/div[2]/div[3]/div[1]/p[2]'
FL_OFI_NUMBERS_NU1_NOCHE = '/html/body/div[3]/div[3]/section[2]/div/div[2]/div[3]/div[1]/p[3]/span[3]'
FL_OFI_NUMBERS_NU2_NOCHE = '/html/body/div[3]/div[3]/section[2]/div/div[2]/div[3]/div[1]/p[3]/span[5]'

FL_OFI_WIND4_FECHA_NOCHE = '/html/body/div[3]/div[3]/section[2]/div/div[2]/div[3]/p[2]'
FL_OFI_WIND4_NU3_NOCHE = '//html/body/div[3]/div[3]/section[2]/div/div[2]/div[3]/p[3]/span[1]'
FL_OFI_WIND4_NU4_NOCHE = '/html/body/div[3]/div[3]/section[2]/div/div[2]/div[3]/p[3]/span[3]'
FL_OFI_WIND4_NU5_NOCHE = '/html/body/div[3]/div[3]/section[2]/div/div[2]/div[3]/p[3]/span[5]'
FL_OFI_WIND4_NU6_NOCHE = '/html/body/div[3]/div[3]/section[2]/div/div[2]/div[3]/p[3]/span[7]'

FLORIDA_OFICIAL_NOCHE = {
    'URL' : [FL_OFI_PAGES_NOCHE,FL_OFI_NUMBERS_NOCHE,FL_OFI_WIND4_NOCHE],
    'TRES' : [FL_OFI_NUMBERS_FECHA_NOCHE,FL_OFI_NUMBERS_NU1_NOCHE,FL_OFI_NUMBERS_NU2_NOCHE],
    'CUATRO' : [FL_OFI_WIND4_FECHA_NOCHE,FL_OFI_WIND4_NU3_NOCHE,FL_OFI_WIND4_NU4_NOCHE,FL_OFI_WIND4_NU5_NOCHE,FL_OFI_WIND4_NU6_NOCHE]
}

FLORIDA_NOCHE_TODO =[FLORIDA_LOTTERY_USA_NOCHE,FLORIDA_OFICIAL_NOCHE ]