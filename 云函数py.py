import requests ,os
# server酱开关，填0不开启(默认)，填2同时开启cookie失效通知和签到成功通知
sever = 'on'
# 填写server酱sckey,不开启server酱则不用填（自己更改）
sckey = 'SCU164694Tbef3710fcd55b01ea1012be369503d026049fe23ed103'
# 填入glados账号对应cookie
cookie = '__cfduid=da0a5d755906104d888c92afef9731ae91615450258; _ga=GA1.2.98364910.1615450268; _gid=GA1.2.1189773139.1615450268; koa:sess=eyJ1c2VySWQiOjM2MjkyLCJfZXhwaXJlIjoxNjQxMzcxMDIwMDY0LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=oIuh2t3Kic9ypxrLmAimIgqYtEk; _gat_gtag_UA_104464600_2=1'
referer = 'https://glados.rocks/console/checkin'

def start():
    
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    origin = "https://glados.rocks"
    referer = "https://glados.rocks/console/checkin"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    payload={
        'token': 'glados_network'
    }
    checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer,'origin':origin,'user-agent':useragent,'content-type':'application/json;charset=UTF-8'},data=json.dumps(payload))
    state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer,'origin':origin,'user-agent':useragent})
   # print(res)

    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        #print(time)
        if sever == 'on':
            requests.get('https://sc.ftqq.com/' + sckey + '.send?text='+mess+'，you have '+time+' days left')
    else:
        requests.get('https://sc.ftqq.com/' + sckey + '.send?text=cookie过期')

def main_handler(event, context):
  return start()

if __name__ == '__main__':
  start()

