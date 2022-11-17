#!/usr/bin/env python3
import json
import time
import requests

def main():
    token = login()
    print(time.strftime('%Y-%m-%d %H:%I:%M:%S',time.localtime(time.time())),'token:',token)
    time.sleep(2)
    while token:
        if heart(token):
            time.sleep(15)
        else:
            time.sleep(5)
            main()



def login():
    loginurl = 'http://58.213.103.4:18080/DGS/sys/login'
    headers = {'Accept':'*/*','Cache-Control':'no-cache', 'Content-Type':'application/json'}
    # base64(rc4(str2utf8(json())))
    data = 'vqpptrI3NntWpcBYaS+Zl7WiBXovdRYfDdZ/ECvugUfrcLzqqaRCGK5SWxazbcvR2ND4KNjyw9cGpDerK3e8TrEQkr9SjhwMmN+tlyY4/pgE0LYU7vEMJMWdng00HVV49wxh9nRqZSJ2kAPHUi0aKZ6sbvnrktrJT+ZOUFBxNp9/jis7l72TtcSHE6lzosLvRQbzqoGvG61HaZJ/pOrw+WIzl5LR1KEKVWQsQoEhXH1BdvgMqQ95rVMjTeuzRocoVNGTMlr0hKl5zlSfiALNtnb1wjoexGLCmXoWMqzoz1n51UZb9ijs2Uh02A1e/FXIEfT/4NXJ+hA2YUTz0x1ye3uyqjSmDxDMn1uv7zymKVZGQR4Bb9t+jWIrpxA9uAeFw2UV4XHehKt9x2zK27e9zCtnLQfmlnPBC1WDoiAI5/ThuZ3Md9ndehlcU8g+U9U/2X+0wIKoTTMX8/dG4dVcDPwZmiA5HCSuwtkuF4mSWie+6liZAEog5gXYb6mccstupLXiVOEWozZJIVGrrNlh1SB1GZRwBrO9PIvseQ7rr2zt514aMaHSjnz5fOSYz3oFlz8WgB8Oj7PkZ70aQvLqN7O2X4impTyM'
    resp = requests.post(url=loginurl,headers=headers,data=data,verify=False,timeout=5)
    if resp.status_code == 200:
        j = json.loads(resp.content)
        if j['success'] == True:
            return j['token']

def heart(token):
    hearturl = 'http://58.213.103.4:18080/DGS/sys/heartBeat'
    headers = {'Accept':'*/*','Cache-Control':'no-cache', 'Content-Type':'application/json','hardid':'7BAEADC5F36845a3B0D4C2CFE0583B5E'}
    data = ''
    cookies = {'SESSION': token}
    response = requests.post(url=hearturl, data=data, headers=headers, cookies=cookies,verify=False,timeout=5)
    if response.status_code == 200:
        j = json.loads(response.content)
        if j['success'] == True:
            if j['retcode'] == 1006:
                print(time.strftime('%Y-%m-%d %H:%I:%M:%S',time.localtime(time.time())),'heartBeat Ok.')
                return True
        else:
            return False


if __name__ == '__main__':
    main()


