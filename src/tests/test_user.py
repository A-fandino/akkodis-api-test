import pytest
from main import create_app
from flask import url_for
from datetime import datetime


def check_all_fields(user: dict):
    assert "id" in user
    assert "name" in user
    assert "email" in user
    assert "cars" in user


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


def test_create_user(client):
    response = client.post(
        url_for("api.user.create_user"), json={"name": "Test", "email": "test@test.com"}
    )
    assert response.status_code == 201
    check_all_fields(response.json[0])
    response = client.post(
        url_for("api.user.create_user"),
        json={"name": "Test", "email": "test@test.com", "extra_fields": "test"},
    )
    assert response.status_code != 201


def test_get_all_users(client):
    response = client.get(url_for("api.user.get_all_users"))
    assert response.status_code == 200
    if len(response.json) > 0:
        check_all_fields(response.json[0])


def test_get_user(client):
    all_users = client.get(url_for("api.user.get_all_users")).json
    user = all_users[0]
    response = client.get(url_for("api.user.get_user", id_=user.get("id")))
    assert response.status_code == 200
    check_all_fields(response.json)


def test_update_user(client):
    all_users = client.get(url_for("api.user.get_all_users")).json
    user = all_users[0]
    new_email = str(datetime.now()) + "a@a.com"
    response = client.patch(
        url_for("api.user.update_user", id_=user.get("id")),
        json={"email": new_email},
    )

    assert response.status_code == 200
    assert response.json.get("email") == new_email


def test_assign_car(client):
    all_users = client.get(url_for("api.user.get_all_users")).json
    user = all_users[0]
    all_cars = client.get(url_for("api.car.get_all_cars")).json
    car = all_cars[0]
    response = client.post(
        url_for("api.user.assign_car", id_=user.get("id")),
        json={"car_ids": [car.get("id")]},
    )
    assert response.status_code == 200


def test_unassign_car(client):
    all_users = client.get(url_for("api.user.get_all_users")).json
    user = all_users[0]
    car = user.get("cars")[0]
    response = client.delete(
        url_for("api.user.unassign_car", id_=user.get("id"), car_id=car.get("id")),
    )
    assert response.status_code == 200


def test_delete_user(client):
    all_users = client.get(url_for("api.user.get_all_users")).json
    user = all_users[-1]
    response = client.delete(url_for("api.user.delete_user", id_=user.get("id")))
    assert response.status_code == 200
    response = client.delete(url_for("api.user.delete_user", id_=user.get("id")))
    assert response.status_code != 200
