import requests
from pprint import pprint
import operator

superhero_list = ['Hulk', 'Captain America', 'Thanos']
url = 'https://akabab.github.io/superhero-api/api/all.json'
responce = requests.get(url)
heroes = []
res = []
def best_intelligence(superhero_list):
      for a in responce.json():
            if a['name'] in superhero_list:
                value = a['powerstats']
                keys_ = value.pop('intelligence')
                heroes.append(a['name'])
                heroes.append(keys_)
                dct = dict(zip(heroes[::2], heroes[1::2]))
                x = max(dct.items(), key=operator.itemgetter(1))
                return x
list_ = []
list_.append(best_intelligence('Hulk'))
list_.append(best_intelligence('Thanos'))
list_.append(best_intelligence('Captain America'))
pprint(f'Максимальное значение интелекта у: {max(list_)} ')


TOKEN = 'y0_AgAAAAA9-SULAADLWwAAAADbRjav2qClUl1cQMWr6qMuwCXDxnbaVaw'

class YandexDisk:


    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")
# if __name__ == '__main__':
#     ya = YandexDisk(token=TOKEN)
#     pprint(ya.upload_file_to_disk(disk_file_path="netology/test23.txt",
#                                   filename="test.txt"))





