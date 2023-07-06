import os
import requests

TOKEN = ''


class YaUploader:
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

    def upload_file_to_disk(self, local_file_path):
        filename = os.path.basename(local_file_path)
        disk_file_path = '/' + filename
        href_json = self._get_upload_link(disk_file_path)
        href = href_json.get("href")
        if href:
            with open(local_file_path, 'rb') as file:
                response = requests.put(href, data=file)
                response.raise_for_status()
                if response.status_code == 201:
                    print("Успех")
        else:
            print(f"Не удалось получить ссылку для загрузки файла {filename} на Яндекс.Диск")


if __name__ == "__main__":
    uploader = YaUploader(token=TOKEN)
    file_path = input("Введите путь до файла на компьютере: ")
    uploader.upload_file_to_disk(file_path)
