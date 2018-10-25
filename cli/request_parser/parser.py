""" """
import urllib.request
import json_config

from bs4 import BeautifulSoup

""" Class for parse aliexpress """
class AliExpressParserRequest:
    result = {}

    def __init__(self):
        self.config = json_config.connect('./config/request.json')

    def _read_base_HTML(self):
        request = urllib.request.Request(self.config['source_link'])
        response = urllib.request.urlopen(request)
        html = response.read()
        
        return html

    def _parse_categories(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        categories_wrapper = soup.find(class_='categories-list-box')

        self.result["categories"] = [{"name": x.dt.text.strip(), "path": x.dd["data-path"], "items": []} for x in categories_wrapper.select('dl')]

        self._parse_sub_categories()

    def _parse_sub_categories(self):
        for category in self.result["categories"]:
            path = str(self.config["sub_category"]).format(path=category["path"])

            request = urllib.request.Request(path)
            response = urllib.request.urlopen(request)
            html = response.read()

            soup = BeautifulSoup(html, 'html.parser')
            sub_categories_list = soup.find_all(class_='sub-cate-items')

            for items in sub_categories_list:
                sub_category = {
                    "name": items.dt.a.text,
                    "items": []
                }

                for inner in items.select("dd a"):
                    sub_category["items"].append({
                        "name": inner.text.strip()
                    })

                category["items"].append(sub_category)


    def get_last_data(self):
        html = self._read_base_HTML()
        self._parse_categories(html)

        return self.result
