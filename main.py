import requests
import json


class Test():
    credentials = 'DOJWqQiqTmoAAAAAAAAAAWDpJWS4smg9rQBlM4jBRhsoJHaRPud__kQQ-6VlDoZc'

    def upload(self):
        url_upload = "https://content.dropboxapi.com/2/files/upload"
        payload_upload = "Rahozin Illia"
        headers_upload = {
            'Dropbox-API-Arg': '{"path": "/zxc.jpg","mode": "add","autorename": true,"mute": false,"strict_conflict": false}',
            'Content-Type': 'application/octet-stream',
            'Authorization': f'Bearer {self.credentials}'
        }

        response_upload = requests.request("POST", url_upload, headers=headers_upload, data=payload_upload)
        return response_upload

    def getFile(self):
        url_gfm = "https://api.dropboxapi.com/2/files/get_metadata"
        payload_gfm = json.dumps({
            "path": "/zxc.jpg"
        })
        headers_gfm = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.credentials}'
        }

        response_gfm = requests.request("POST", url_gfm, headers=headers_gfm, data=payload_gfm)
        return response_gfm

    def deleteFile(self):
        # Delete request
        url_delete = "https://api.dropboxapi.com/2/files/delete_v2"
        payload_delete = json.dumps({
            "path": "/zxc.jpg"
        })
        headers_delete = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.credentials}'
        }

        response_delete = requests.request("POST", url_delete, headers=headers_delete, data=payload_delete)
        return response_delete


if __name__ == '__main__':
    func = Test()
    func.upload()
    func.getFile()
    func.deleteFile()
