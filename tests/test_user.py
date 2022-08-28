from vault.user import User

def test_get_attribute():
    """Test Attribute is obtained properly"""
    user_name = 'test_user'
    user = User(user_name__v = user_name)

    assert user.user_name__v == 'test_user'

def test_is_boolean(vault_session):
    """Test some attributes are correctly parsed as Boolean From API Call"""
    me = vault_session.me
    assert isinstance(me.user_needs_to_change_password__v, bool)

def test_is_datetime(vault_session):
    """Test created_date is pendulum datetime format""" 