from requests import request
from functools import wraps

import requests
def request(**kw):
    def outer(f):
        @wraps(f)
        def inner(**p):
            method = kw['method']
            url = kw['url']
            params = p['data']
            headers = kw.update(kw['headers'])
            # cookies = kw.update(kw['cookies'])
            jar = add_cookie(cookies)
            if method == 'GET':
                if kw['dtype'] == 'params':
                    return requests.request(method, url, params=p['data'],cookies=jar)
                else:
                    print("请检查dtype类型")
            elif method == 'POST':
                if kw['dtype'] == 'data':
                    r=requests.request(method, url, data=p['data'],cookies=jar)
                    return f(r.text)
                elif kw['dtype'] == 'json':
                    r=requests.request(method, url, json=p['data'],cookies=jar)
                    return f(r.text),
                else:
                    print("请检查dtype类型")
            else:
                print("暂时不支持其他方式")
        return inner
    return outer

@request(method='GET',dtype = 'params',url='https://m.mall.autohome.com.cn',headers={'content_type':'application/x-www-form-urlencoded'},cookies={})
def get_api(text,**p):
    print('hello')
    return text



def add_cookie(cookielist):
    jar = requests.cookies.RequestsCookieJar()
    for i in cookielist:

        jar.set(i.pop('name'),i.pop('value'),**i)

    return jar







