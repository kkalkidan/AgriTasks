import pytest

SERVER_URL=http://localhost:5000 pyte

import requests
import os
def test_demo():
   response = requests.get(os.environ['SERVER_URL'] + '/demo')
   assert(response.status_code == 200)

# @pytest.fixture
# def smtp_connection():
#     import smtplib
#     return smtplib.SMTP("0.0.0c.0", 5000, timeout=5)

# def test_ehlo(smtp_connection):
#     response, msg = smtp_connection.ehlo()
#     assert response == 200
#     assert 0

