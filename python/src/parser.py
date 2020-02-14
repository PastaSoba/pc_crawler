import requests
import lxml.html
import datetime
from pc_model import PC_Model

class Parser(object):
    URL = "http://www.lenovo.com/jp/ja/notebooks/thinkpad/e-series/E495/p/22TP2TEE495"
    UA = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    headers = {"User-Agent": UA}

    def __init__(self):
        pass #暫定
        
    def _getName(self, index:int):
        """
        index番目の商品の名前を返す
        
        param
        -----
        index:int - 商品の
        
        """

    def main(self):
        r = requests.get(Parser.URL, headers=Parser.headers)
        html = r.text
        root = lxml.html.fromstring(html)

        # データを取得する
        name = root.cssselect("li.tabbedBrowse-productListing-container:nth-child(1) > div:nth-child(6) > div:nth-child(2) > h3:nth-child(1)")
        price = root.cssselect("li.tabbedBrowse-productListing-container:nth-child(1) > div:nth-child(6) > div:nth-child(3) > div:nth-child(1) > dl:nth-child(1) > dd:nth-child(4)")
        processor = root.cssselect("li.tabbedBrowse-productListing-container:nth-child(1) > div:nth-child(6) > div:nth-child(4) > div:nth-child(3) > div:nth-child(1) > dl:nth-child(2) > dd:nth-child(2)")
        memory = root.cssselect("li.tabbedBrowse-productListing-container:nth-child(1) > div:nth-child(6) > div:nth-child(4) > div:nth-child(3) > div:nth-child(1) > dl:nth-child(2) > dd:nth-child(6)")
        aquired_at = datetime.datetime.now()


        # データを加工する
        name = name[0].text.strip()
        price = price[0].text
        processor = processor[0].text.strip()
        memory = memory[0].text.strip()
        dic = {"name": name, "price": price, "processor": processor, "memory": memory, "aquired_at": aquired_at}

        # モデルを作る
        pc = PC_Model(**dic)

