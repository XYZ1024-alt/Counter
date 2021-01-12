from threading import Thread
import requests

#以下内容皆需抓包
url = 'https://busuanzi.ibruce.info/busuanzi?jsonpCallback=BusuanziCallback_1046179423126'
headers = {
    'Origin': 'https://xyz1024.top/',
    'Referer': 'https://xyz1024.top/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36' #除了这个
}

def count(i):
    try:
        r = requests.get(url=url, headers=headers, timeout=3)
        if r.status_code == 200:
            print('成功')
        else:
            return None
    except:
        pass

def main():
    for i in range(100): #在这输入刷的次数
        t = Thread(target=count, args=(i, ))
        t.start()

if __name__ == '__main__':
    main()