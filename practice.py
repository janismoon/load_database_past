import requests
from pandas import DataFrame

w = "BTC"

x1 = ["2018", "2019", "2020"]
y1 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
z1 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
      "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
# 하루 뒤부터 추출 시작되니 참고

t = []
op = []
hp = []
lp = []
tp = []
db = {'time': t, 'Open Price': op, 'High Price': hp, 'Low Price': lp, 'Trade Price': tp}
for x in x1:
    for y in y1:
        for z in z1:
            url = "https://crix-api-endpoint.upbit.com/v1/crix/candles/minutes/10?code=CRIX.UPBIT.KRW-" + w + \
                  "&count=144&to=" + x + "-" + y + "-" + z + "%2015:00:00"

            r = requests.get(url)
            coin = r.json()
                    
            num = 143
            while num >= 0:
                d = coin[num]
                        
                t.append(d['candleDateTime'])
                op.append(d['openingPrice'])
                hp.append(d['highPrice'])
                lp.append(d['lowPrice'])
                tp.append(d['tradePrice'])
                        
                num = num - 1
                        
database = DataFrame(db)
database.drop_duplicates()
database.to_excel("D:\\문승준\\코인 자동거래\\coin\\" + w + ".xlsx")
