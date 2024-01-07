import requests

def test_mobile():
    params =  {
        "shouji":"15705187072",
        "appkey":"0c818521d38759e1"
    }
    r = requests.get(url="http://sellshop.5istudy.online/sell/shouji/query", params=params)
    assert r.status_code == 200
    res = r.json()
    assert res['status'] == 1
    assert res['msg'] == "ok"
    assert res['result']["shouji"] == "15705187072"
