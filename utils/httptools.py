__author__ = 'qjn'
import requests
def request(url,method,dtype,body=None,headers=None,cookies=None,**kwargs):
    headers = headers or {}
    cookies = cookies or []
    jar = add_cookie(cookies)

    if method=='GET':
        if dtype=='params':
            return requests.request(method, url, params=body, cookies=jar, **kwargs)
        else:print("请检查dtype类型")
    elif method=='POST':
        if dtype == 'data':
            return requests.request(method, url, data=body, cookies=jar, **kwargs)
        elif dtype=='json':
            return requests.request(method, url, json=body, cookies=jar, **kwargs)
        else:print("请检查dtype类型")
    else:
        print("暂时不支持其他方式")


def add_cookie(cookielist):
    jar = requests.cookies.RequestsCookieJar()
    for i in cookielist:
        if all([i.get(j,None) for j in ['name','value']]):
            jar.set(**i)
        else:
            raise ValueError('cookie格式不正确')
    return jar






