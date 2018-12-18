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




cookies = [
    {'name': 'o2oPlatform_user_info_new',
     'value': '"8XySwwrb08Ppy6cQeDMeRdP9M4ypPSA2g1nDiwiBW/g3rsYWlBIVROeuhKhH4AYeO4UuSwdTE0dv9sZ5tEV7jA=="',
     'domain': '.mall.autohome.com.cn', 'path': '/'},
    {'name': 'JSESSIONID', 'value': 'e740c956-427e-4879-b2aa-3e6e9c0030fb',
     'domain': 'tseller.mall.autohome.com.cn', 'path': '/'}
]
@request(method='POST',dtype = 'data',url='http://tseller.mall.autohome.com.cn/carResource/addResource',headers={'content_type':'application/x-www-form-urlencoded'},cookies=cookies)
def post_api(text,**p):
    print('打印结果：')
    return text


if __name__=='__main__':
    # a={'is_app':1}
    # print(get_api(data=a))

    bodys = {
        'operateType': 1,
        'providerId': '81000025',
        'provinceId': 110000,
        'provinceName': '北京',
        'cityId': 110100,
        'cityName': '北京',
        'categoryId': 1,
        'categoryName': '中规车',
        'brandId': 27,
        'brandName': '北京',
        'seriesId': 3800,
        'seriesName': '北京(BJ)20',
        'specId': 33471,
        'specName': '2018款1.5T手动舒适型',
        'isToB': 0,
        'isFreePost': 0,
        'price': 90000,
        'stockNum': 4,
        'contactMan': '秦楠',
        'contactPhone': 18601091164,
        'address': '北京中航',
        'deliveryProvinceCity': '''[
        {"provinceId": "110000", "provinceName": "北京", "areaCityList": [{"cityId": "110100", "cityName": "北京"}]},
        {"provinceId": "500000", "provinceName": "重庆", "areaCityList": [{"cityId": "500100", "cityName": "重庆"}]}]''',

        'props': '''[{"colorPropId": "562199", "colorPropName": "冰晶蓝", "innerPropId": "562204", "innerPropName": "黑色",
             "price": "120000", "stockNum": "1"},
            {"colorPropId": "562200", "colorPropName": "极光绿", "innerPropId": "562204", "innerPropName": "黑色",
             "price": "100000", "stockNum": "1"},
            {"colorPropId": "562199", "colorPropName": "冰晶蓝", "innerPropId": "585477", "innerPropName": "黑色",
             "price": "100000", "stockNum": "1"},
            {"colorPropId": "562200", "colorPropName": "极光绿", "innerPropId": "585477", "innerPropName": "黑色",
             "price": "90000", "stockNum": "1"}]'''
    }
    print(post_api(data=bodys))



