import pytest
from main import create_app
from flask import url_for
from datetime import datetime


def check_all_fields(car: dict):
    assert "id" in car
    assert "name" in car
    assert "brand" in car


@pytest.fixture()
def app():
    app = create_app()
    app_ctx = app.app_context()
    app_ctx.push()
    return app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_create_car(client):
    response = client.post(
        url_for("api.car.create_car"), json={"name": "Test", "brand": "Seat"}
    )
    assert response.status_code == 201
    check_all_fields(response.json[0])
    response = client.post(
        url_for("api.car.create_car"),
        json={"name": "Test", "brand": "Seat", "extra_fields": "test"},
    )
    assert response.status_code != 201


def test_get_all_cars(client):
    response = client.get(url_for("api.car.get_all_cars"))
    assert response.status_code == 200
    if len(response.json) > 0:
        check_all_fields(response.json[0])


def test_get_car(client):
    all_cars = client.get(url_for("api.car.get_all_cars")).json
    car = all_cars[0]
    response = client.get(url_for("api.car.get_car", id_=car.get("id")))
    assert response.status_code == 200
    check_all_fields(response.json)


def test_update_car(client):
    all_cars = client.get(url_for("api.car.get_all_cars")).json
    car = all_cars[0]
    new_brand = str(datetime.now())
    response = client.patch(
        url_for("api.car.update_car", id_=car.get("id")),
        json={"brand": new_brand},
    )

    assert response.status_code == 200
    assert response.json.get("brand") == new_brand


def test_delete_car(client):
    all_cars = client.get(url_for("api.car.get_all_cars")).json
    car = all_cars[-1]
    response = client.delete(url_for("api.car.delete_car", id_=car.get("id")))
    assert response.status_code == 200
    response = client.delete(url_for("api.car.delete_car", id_=car.get("id")))
    assert response.status_code != 200
