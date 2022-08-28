import pytest
import requests
from vault.error import InvalidVersion, ClientError
from vault import Vault

def test_invalid_version():
    """Test InvalidVersion is raised if an Invalid Version number is passed as input to the Vault class"""
    
    with pytest.raises(InvalidVersion):
        vault = Vault(
            'username',
            'password',
            'vault_subdomain',
            '15.1'
        )

def test_invalid_username(credentials):
    """Test error is raised if wrong credentials"""
    credentials['AUTH']['username'] = 'wrong_user'
    
    with pytest.raises(ClientError):
        vault = Vault(
            **credentials['AUTH']
        )

def test_me_object_returns_correct_values(vault_session):
    """It is expected the current username has the same username used for the login"""
    assert vault_session.me._user_name__v == vault_session.username
    
    
