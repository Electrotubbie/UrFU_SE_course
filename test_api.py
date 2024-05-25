from fastapi.testclient import TestClient
from api import app
from unmask import unmasker

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message':
        "С помощью рассматриваемой модели выполняется "
        "заполнение пропущенного слова на наиболее подходящее. "
        "В качестве входных данных принимается предложение "
        "с помеченным <mask> пропущенным словом."
        }


def test_unmask_api():
    text = "Try to test <mask> application."
    response = client.post("/unmask/", json={"text": text})
    json_data = response.json()
    unmask_data = unmasker(text)
    assert response.status_code == 200
    assert json_data == unmask_data


def test_unmask_result():
    text = "Today is a <mask> weather."
    response = client.post("/unmask/", json={"text": text})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data[0]['sequence'] == 'Today is a beautiful weather.'
    assert json_data[1]['sequence'] == 'Today is a nice weather.'
    assert json_data[2]['sequence'] == 'Today is a gorgeous weather.'
    assert json_data[3]['sequence'] == 'Today is a perfect weather.'
    assert json_data[4]['sequence'] == 'Today is a hot weather.'
