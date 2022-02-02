from tracks_sdk.controllers.track_controller import TrackController


def test_set_path():
    controller = TrackController()

    path = "/home"
    controller.with_path(path)

    assert controller.path == path


def test_set_path():
    controller = TrackController()

    event_data = {
        "is_logged": True
    }

    controller.with_event_data(event_data)

    assert controller.event_data == event_data