import requests
import hashlib
from urllib.parse import urlencode,unquote


class VMQ(object):

    def __init__(self,payment='wechat'):
        from service.util.pay.pay_config import get_config
        self.web_url = get_config('web_url')
        if payment == 'wechat':
            config = get_config('V免签微信')
            self.v_type = 1
        else:
            config = get_config('V免签支付宝')
            self.v_type = 2
        self.key = config['KEY']   #填写通信密钥
        self.host_api = config['API']
        self.notify = self.web_url + '/notify/vmq'

    def create_order(self,name,out_trade_no,total_price):
        if total_price % 1 == 0:
            total_price = int(total_price)
        data = {
            'payId':out_trade_no,
            'type':self.v_type,
            'price':total_price,
            'param':out_trade_no,
            'notifyUrl':self.notify
        }        
        data['sign'] = hashlib.md5((data['payId']+str(data['param'])+str(data['type'])+str(data['price'])+self.key).encode('utf8')).hexdigest()

        r = requests.post(self.host_api+'/createOrder',json=data)
        # print(r.text)
        if r.status_code == 200:
            if r.json()['code'] == 1:
                # return r.json()['data']     # 包含payUrl,orderId
                res = r.json()['data']
                return {'qr_code':res['payUrl'],'payjs_order_id':res['orderId'],'reallyPrice':res['reallyPrice'],'redirect':2} # 第三方状态1；本地2
            elif r.json()['code'] == -1:
                print(r.json())
                return {'qr_code':"手机监控端状态掉线，请检查后再重试"}
            else:
                print(str(r.json()))
                return False
        else:
            print(r.text)
        return False

    def check(self,orderId):     #这里是上一步主动生成的订单，单独调用
        data = {
            'orderId': orderId
        }
        r = requests.post(self.host_api+'/checkOrder',json=data)
        if r.status_code == 200:
            if r.json()['code'] == 1:
                return True
        return False

    def verify(self,data):     #异步通知    这里data=request.from
        try:
            signature = data['sign']
            data.pop('sign')
            # print(hashlib.md5((data['payId']+str(data['param'])+str(data['type'])+str(data['price'])+str(data['reallyPrice'])+self.key).encode('utf8')).hexdigest())
            return signature == hashlib.md5((data['payId']+str(data['param'])+str(data['type'])+str(data['price'])+str(data['reallyPrice'])+self.key).encode('utf8')).hexdigest()   # 结果为一个布尔值
        except Exception as e:
            print(e)
            return False    
        