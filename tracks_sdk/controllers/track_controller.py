from tracks_sdk.models.track import Track
from tracks_sdk.services.melidata_api import MelidataApi


class TrackController:
    def __init__(self):
        self.path = ""
        self.event_data = {}

    def with_event_data(self, event_data):
        self.event_data = event_data

    def with_path(self, path):
        self.path = path

    def _build(self):
        track = Track(self.path, self.event_data)
        return dict(track)

    def send_track(self):
        track = self._build()
        if not MelidataApi.post_track(track):
            raise Exception("Error to send track")

        return True
