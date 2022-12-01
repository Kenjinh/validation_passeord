import json
from flask import url_for
def test_rest_api(client):
    data ={
        "password": "TesteSenhaForte!123&",
        "rules": [
            {"rule": "minSize","value": 8},
            {"rule": "minSpecialChars","value": 2},
            {"rule": "noRepeted","value": 0},
            {"rule": "minDigit","value": 4}
            ]
    }
    response_200 = {
        'noMatch': [],
        'verify': True
    }
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    url = url_for('verify.verify')
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 200
    assert response.json == response_200