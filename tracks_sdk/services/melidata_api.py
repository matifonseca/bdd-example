import requests


class MelidataApi:
    URL = "https://internal-api.mercadolibre.com/internal/tracks"

    @staticmethod
    def post_track(track):
        response = requests.post(MelidataApi.URL, json=track)
        return response.status_code == 201
