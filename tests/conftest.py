import requests
import pytest
import logging

from config import APP_URL, ADMIN_USER, ADMIN_PASSWORD, LOG

@pytest.fixture(scope="session")
def login_as_admin():
  LOG.info("login_as_admin()")
  payload = {"username":ADMIN_USER, "password":ADMIN_PASSWORD}
  LOG.debug(f"Login payload: {payload}")
  response = requests.post(f"{APP_URL}/auth/login", data=payload)
  assert response.ok

  access_token = response.json()["access_token"]
  yield access_token
