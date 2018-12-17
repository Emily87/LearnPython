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




# def add_cookie(cookielist):
#     jar = requests.cookies.RequestsCookieJar()
#     for i in cookielist:
#
#         jar.set(i.pop('name'),i.pop('value'),**i)
#
#     return jar

if __name__ == '__main__':
    cookies = [
        {'name': 'o2oPlatform_user_info_new',
         'value': '"G1sBl1Ou9Nsv86zipIVP5RQ2gfAfKuopSuEtsEWAz2xjoY/mwahZvRfJmqPVV82Qj2dtCMgzM3piWSOK68HUWg=="',
         'domain': '.mall.autohome.com.cn', 'path': '/'},
        {'name': 'JSESSIONID', 'value': '5c4e499c-819f-4f2b-84d4-5649a3e9586b',
         'domain': 'tseller.mall.autohome.com.cn', 'path': '/'}
    ]

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
    headers = {
        'Content-Length': '2069', 'Content-Type': 'application/x-www-form-urlencoded'
    }
    #headers['host']='tseller.mall.autohome.com.cn'
    # res = request('http://tseller.mall.autohome.com.cn/brandCarResource/list?checkStatus=0','get',{},cookies=cookies)
    res = request("http://tseller.mall.autohome.com.cn/carResource/addResource", 'POST','data', body=bodys,
                  cookies=cookies)
    # res = request("http://10.168.66.131/carResource/addResource", 'POST', 'data', body=bodys,headers=headers,
    #               cookies=cookies)

    print(res.text)
    print(res.status_code)

