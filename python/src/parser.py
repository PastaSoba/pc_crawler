import requests
import datetime
import re
from bs4 import BeautifulSoup 

class Parser:
    """
    URLにアクセスして、パソコンの情報を含んだデータをかえす（仮）
    """
    URL = "http://www.lenovo.com/jp/ja/notebooks/thinkpad/e-series/E495/p/22TP2TEE495"

    @staticmethod
    def _getSoupFromURL(url: int):
        """
        urlのリンク先のsoupを返す
        parameter
        -----
        url : str
            読み込みたいページのurl
        
        return
        -----
        soup : Beautifulsoup.soup
            読み込んだページのsoupオブジェクト？
        """
        UA = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
        headers = {"User-Agent": UA}
        # スクレイピング対象の URL にリクエストを送り HTML を取得する
        res = requests.get(Parser.URL, headers=headers)
        # レスポンスの HTML から BeautifulSoup オブジェクトを作る
        soup = BeautifulSoup(res.text, 'html.parser')
        return soup
        
    @staticmethod
    def main():
        page = Parser._getSoupFromURL(Parser.URL)
        result = []
        # データを取得する
        items = page.find_all("div", {"class":"tabbedBrowse-productListing"})
        for item in items:
            not_striped_name = item.find("h3", {"class":"tabbedBrowse-productListing-title"}).text.strip()
            name = re.sub("<.*>","",not_striped_name)
            price = item.find("dd", {"class":"saleprice pricingSummary-details-final-price"}).text
            processor = item.find("div", {"class": "expandableContent tabbedBrowse-productListing-expandableContent-features expandableContent-is-collapsed"}).find_all("dd")[0].text
            memory = item.find("div", {"class": "expandableContent tabbedBrowse-productListing-expandableContent-features expandableContent-is-collapsed"}).find_all("dd")[2].text

            # データを加工する
            dic = {"name": name, "price": price, "processor": processor, "memory": memory}
            result.append(dic)
        return result