import pytest
from securimage_solver import CaptchaApi

def test_CaptchApi():
    c = CaptchaApi()
    predicted_value = c.predict(r'images\7NwHCn_141c1458-b5e4-439f-be01-8a8b30c6cbd8.png')
    assert predicted_value == '7NwHCn'
