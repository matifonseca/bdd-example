from tracks_sdk.models.track import Track


def test_track_to_json():
    path = "/home"
    event_data = {
        "is_logged": True
    }
    track = Track(path=path,
                  event_data=event_data)

    assert dict(track) == {
        "path": path,
        "event_data": event_data
    }