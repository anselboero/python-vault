import configparser
import os
import pytest
from vault.vault import Vault

CONFIG_PATH = os.path.join('tests','auth.conf')

@pytest.fixture
def credentials():
    conf = configparser.ConfigParser()

    conf.read(CONFIG_PATH)
    return conf

@pytest.fixture
def vault_session(credentials):
    """The function logs the user in order to avoid logging maximum burst limit"""
    vault = Vault(
        **credentials['AUTH']
    )
    return vault
