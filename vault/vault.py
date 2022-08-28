import requests
from vault.error import InvalidVersion, ClientError
from vault.user import User

SUPPORTED_VERSIONS = ['22.3']

class Vault():
    """Entry Point class that provides high-level access to the Veeva Vault API methods.
    args:
        username: The Vault username
        password: The Vault Password
        vault_subdomain: The DNS of the Vault for which you want to generate a session.
        version: The Vault REST API version.
    """

    def __init__(self,
        username: str, 
        password: str, 
        vault_subdomain: str, 
        version: str
        ):
        if version not in SUPPORTED_VERSIONS:
            raise (InvalidVersion(f"Version {version} is invalid or not supported."
                f"Supported Versions are {', '.join(SUPPORTED_VERSIONS)}"))
        
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        self.username = username
        self.password = password
        self.vault_subdomain = vault_subdomain
        self.version = f"{version}"
        self.base_url = f"https://{self.vault_subdomain}/api/v{self.version}"
        self.session = requests.Session()
        self.session.headers.update(headers)
        self.session_id = None
        # Call the auth method and stores the SessionId into the requests.session headers
        self.auth()
        # User Object containing information about user.
        self._me = None
        

    
    def _post(
        self,
        endpoint: str,
        data: dict = {},
    ):
        """Sends Post Method"""
        req = self.session.post(
            f'{self.base_url}/{endpoint}',
            data = data
        )
        self._check_response_status(req)
        return req
    
    def _get(
        self,
        endpoint: str
    ):
        """Sends Get Method"""
        req = self.session.get(
            f'{self.base_url}/{endpoint}'
        )
        self._check_response_status(req)
        return req
    
    def _check_response_status(
        self,
        request
    ):
        """Checks if the responseStatus of the Requests is Success or Failure.
        If FAILURE it raises a ClientError"""
        if request.json()['responseStatus'] == 'FAILURE':
            raise ClientError(request.json())

    def auth(
            self, 
            username: str = None, 
            password: str = None
    ):
        """Runs https://developer.veevavault.com/api/22.3/#user-name-and-password method
        and stores the SessionId into the requests.Session headers.
        Also updates The sessionID in case it is expired (TBD)"""
        if username:
            self.username = username
        if password:
            self.password = password

        endpoint = 'auth'
        data = {
            'username': self.username,
            'password': self.password
        }
        req = self._post(endpoint, data)
    
        response_data = req.json()
        self.session_id = response_data['sessionId']
        self.session.headers.update({'Authorization': self.session_id})
        return req
    
    @property
    def me(self) -> User:
        """Class VaultObject.User: User instance related to the Current User."""
        if self._me is None:
            self._me = self.get_user('me')
        return self._me
    
    def get_user(self, id) -> User:
        """Runs https://developer.veevavault.com/api/XX.x/#retrieve-user Method"""
        endpoint = f'objects/users/{id}'
        # Information about the Current User
        user_data = self._get(endpoint).json()['users'][0]['user']
        user_obj = User.de_json(user_data)
        return user_obj
    





