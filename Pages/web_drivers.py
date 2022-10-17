from lib2to3.pgen2 import driver
from typing_extensions import Self
import webbrowser
import pytest
from selenium import webdriver
from soupsieve import select
from extract_dict import json_dict

@pytest.fixture(scope='session')
class web_driver(webbrowser.Chrome):
    def __init__(self, capabilities: dict.__dict__.__class__) -> None:
        self.desired_capabilities = capabilities
        for key in webdriver.DesiredCapabilities.CHROME.items().__iter__():
            self.desired_capabilities.setdefault(key[0], key[1])
        self = _drivers_autoselect(self.desired_capabilities)

class _drivers_autoselect:
    '''
    The Vehicle object contains lots of vehicles
    :param arg: The arg is used for ...
    :type arg: str
    :param `*args`: The variable arguments are used for ...
    :param `**kwargs`: The keyword arguments are used for ...
    :ivar arg: This is where we store arg
    :vartype arg: str
    '''
    def __init__(self, capabilities: dict.__dict__.__class__) -> webdriver.Remote.__class__:  # type: ignore
        '''We can't travel a certain distance in vehicles without fuels, so here's the fuels

        :param `capabilities`: The amount of distance traveled
        :type `capabilities`: dict[str, Any]
        :param bool destinationReached: Should the fuels be refilled to cover required distance?
        :raises: :class:`RuntimeError`: Out of fuel

        :returns: the webdriver selected by 'browserName' from `capabilities`
        :rtype: webdriver.Remote.__class__
        ''' 
        self.desired_capabilities = capabilities
        self._driver: webdriver.__spec__
        yield __loader__()
        return self._driver
    @__loader__
    def _chrome(self):
        with self.desired_capabilities['browserName'].lower() == 'chrome':
            self._driver = webdriver.Chrome(desired_capabilities=self.desired_capabilities)
    @__loader__
    def _firefox(self):
        with self.desired_capabilities['browserName'].lower() == 'firefox':
            self._driver = webdriver.Firefox(desired_capabilities=self.desired_capabilities)
    @__loader__
    def _edge(self):
        with self.desired_capabilities['browserName'].lower() == 'msedge':
            self._driver = webdriver.Edge(str(self.desired_capabilities))
