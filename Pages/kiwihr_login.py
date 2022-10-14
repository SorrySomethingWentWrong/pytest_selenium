from extract_dict import json_dict
from web_drivers import web_driver


class kiwihr_login_page(web_driver):
    global _driver
    def __init__(self, driver) -> None:
        # Les info de connexion du site KiwiHR
        self.info: dict.__dict__.__class__ = json_dict('kiwihr_login.py')
    