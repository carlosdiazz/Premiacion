from Orkapi2 import Premio
from obtenerNumeros3 import Numeros

xpath_LOTTERY_POST_NY = [
    'https://www.lotterypost.com/game/146/results',
    '//*[@id="resultsTable"]/table/tbody/tr[1]/td/div/div[1]',
    '//*[@id="resultsTable"]/table/tbody/tr[1]/td/div/div[2]/div[2]/ul/li[2]',
    '//*[@id="resultsTable"]/table/tbody/tr[1]/td/div/div[2]/div[2]/ul/li[3]',
    'https://www.lotterypost.com/game/149/results',
    '//*[@id="resultsTable"]/table/tbody/tr[1]/td/div/div[1]',
    '//*[@id="resultsTable"]/table/tbody/tr[1]/td/div/div[2]/div[2]/ul/li[1]',
    '//*[@id="resultsTable"]/table/tbody/tr[1]/td/div/div[2]/div[2]/ul/li[2]',
    '//*[@id="resultsTable"]/table/tbody/tr[1]/td/div/div[2]/div[2]/ul/li[3]',
    '//*[@id="resultsTable"]/table/tbody/tr[1]/td/div/div[2]/div[2]/ul/li[4]'
]

xpath_LOTTERY_USA_NY = [
    'https://www.lotteryusa.com/new-york/numbers/',
    '//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time',
    '//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span',
    '//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[3]/span',
    'https://www.lotteryusa.com/new-york/win-4/',
    '//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time',
    '//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[1]/span',
    '//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span',
    '//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[3]/span',
    '//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[4]/span'
]

xpath_LOTTERY_POST_FL = [
    'https://www.lotterypost.com/game/33/results',
    '//*[@id="resultsTable"]/table/tbody/tr[1]/td/div/div[1]',
    '//*[@id="resultsTable"]/table/tbody/tr[1]/td/div/div[2]/div[2]/ul/li[2]',
    '//*[@id="resultsTable"]/table/tbody/tr[1]/td/div/div[2]/div[2]/ul/li[3]',
    'https://www.lotterypost.com/game/37/results',
    '//*[@id="resultsTable"]/table/tbody/tr[1]/td/div/div[1]',
    '//*[@id="resultsTable"]/table/tbody/tr[1]/td/div/div[2]/div[2]/ul/li[1]',
    '//*[@id="resultsTable"]/table/tbody/tr[1]/td/div/div[2]/div[2]/ul/li[2]',
    '//*[@id="resultsTable"]/table/tbody/tr[1]/td/div/div[2]/div[2]/ul/li[3]',
    '//*[@id="resultsTable"]/table/tbody/tr[1]/td/div/div[2]/div[2]/ul/li[4]'
]


xpath_LOTTERY_USA_FL = [
    'https://www.lotteryusa.com/florida/pick-3/',
    '//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time',
    '//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span',
    '//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[3]/span',
    'https://www.lotteryusa.com/florida/pick-4/',
    '//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time',
    '//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[1]/span',
    '//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span',
    '//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[3]/span',
    '//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[4]/span'
]

url = 'https://dev_admin.orkapi.net/'

Numeros_lottery_post_NY = Numeros(xpath_LOTTERY_POST_NY).obtener_Todo()
Numeros_lottery_USA_NY = Numeros(xpath_LOTTERY_USA_NY).obtener_Todo()

print(Numeros_lottery_post_NY)
print(Numeros_lottery_USA_NY)

if(Numeros_lottery_post_NY and Numeros_lottery_USA_NY == Numeros_lottery_post_NY):
    Premio(url,'carlos@orkapi',1234,'New York', Numeros_lottery_post_NY )

Numeros_lottery_POST_FL = Numeros(xpath_LOTTERY_POST_FL).obtener_Todo()
Numeros_lottery_USA_FL = Numeros(xpath_LOTTERY_USA_FL).obtener_Todo()

if(Numeros_lottery_POST_FL and Numeros_lottery_POST_FL == Numeros_lottery_USA_FL ):
    Premio(url, 'carlos@orkapi',1234,'loteria', Numeros_lottery_USA_FL )