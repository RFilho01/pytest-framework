import requests
import pytest

def test_health():
    response = requests.get("http://localhost:8080/health")
    assert response.ok