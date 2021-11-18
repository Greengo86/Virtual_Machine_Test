import requests


class VirtualMachineService:
    """
    API от Яндекс Cloud. https://cloud.yandex.ru/docs/compute/operations/vm-create/create-linux-vm
    Отказано в доступе в сети - возможно из-за того, что всё-таки TRIAL FREE. Плюс если передам свои данные из формы -
    АПИ будет ругаться на неверные данные. Поэтому нужна API не с бесплатным периодом и с хорошей документацией
    """

    api_token = ''

    def create_vm(self, data_form):
        token = self.get_token()
        url = 'https://compute.api.cloud.yandex.net/compute/v1/instances'
        headers = {"Authorization": f"Bearer {token}"}
        folder = self.get_folder()
        data = {
            "folderId": f"{folder}",
            "name": "instance-demo-no-pwauth",
            "zoneId": "ru-central1-c",
            "platformId": "standard-v3",
            "resourcesSpec": {
                "memory": data_form['ram'] * 1024,
                "cores": data_form['cpu'],
            },
            "metadata": {
                "user-data": f"#cloud-config\nusers:\n  - name: {data_form['name']}\n    groups: sudo\n    shell: /bin/bash\n    sudo: ['ALL=(ALL) NOPASSWD:ALL']\n    ssh-authorized-keys:\n      - ssh-rsa AAAAB3N... user@example.com"
            },
            "bootDiskSpec": {
                "diskSpec": {
                    "size": "2621440000",
                    "imageId": "fd8rc75pn12fe3u2dnmb"
                }
            },
            "networkInterfaceSpecs": [
                {
                    "subnetId": "b0ccabo6de5u6jq69qci",
                    "primaryV4AddressSpec": {
                        "oneToOneNatSpec": {
                            "ipVersion": "IPV4"
                        }
                    }
                }
            ]
        }
        return requests.post(url, json=data, headers=headers).json()['message']

    def get_folder(self):
        token = self.get_token()
        my_cloud_id = 'b1gudgcohdlimior9hgd'
        url = f'https://resource-manager.api.cloud.yandex.net/resource-manager/v1/folders?cloudId={my_cloud_id}'
        headers = {"Authorization": f"Bearer {token}"}
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            #  Забираем нужный нам folder
            return res.json()['folders'][0]['id']
        else:
            raise Exception('Bad request on folder')

    def get_token(self):
        if not VirtualMachineService.api_token:
            # Мой личный токен!!!! Удалить!!!
            data = {"yandexPassportOauthToken": "AQAAAAADxzoTAATuwdpWbJ_ZNU94pkuJU67MZtE"}
            res = requests.post('https://iam.api.cloud.yandex.net/iam/v1/tokens', json=data)
            if res.status_code == 200:
                VirtualMachineService.api_token = res.json()['iamToken']
            else:
                raise Exception('Bad request on api_token')
        return VirtualMachineService.api_token
