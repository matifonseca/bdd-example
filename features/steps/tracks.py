import pytest
import requests_mock
from behave import *

from tracks_sdk.controllers.track_controller import TrackController


@given('que quiero trackear para el path "{}" y si el usuario esta logeado')
def step_impl(context, path):
    """
    :param path: string
    :type context: behave.runner.Context
    """

    context.vars["path"] = path
    context.vars["event_data"] = {
        "is_logged": True
    }


@when("creo el track")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    path = context.vars["path"]
    event_data = context.vars["event_data"]
    controller = TrackController()
    controller.with_path(path)
    controller.with_event_data(event_data)
    context.vars["controller"] = controller


@then("se me informa que se creo correctamente")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    status = context.vars.get("status", 201)
    json_headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # dentro de este bloque "with", todas las llamadas a la librería "requests"
    # pueden ser interceptadas por medio de lalibrería requests_mock
    with requests_mock.Mocker(real_http=True) as m:
        m.post(
            "https://internal-api.mercadolibre.com/internal/tracks",
            headers=json_headers,
            status_code=status
        )

        controller = context.vars["controller"]
        assert controller.send_track()


@step("ocurre un error al enviarlo")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.vars["status"] = 500


@then("se me informa que no se pudo enviar el track")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    with pytest.raises(Exception) as e_info:
        status = context.vars.get("status", 201)
        json_headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        # dentro de este bloque "with", todas las llamadas a la librería "requests"
        # pueden ser interceptadas por medio de lalibrería requests_mock
        with requests_mock.Mocker(real_http=True) as m:
            m.post(
                "https://internal-api.mercadolibre.com/internal/tracks",
                headers=json_headers,
                status_code=status
            )

            controller = context.vars["controller"]
            controller.send_track()