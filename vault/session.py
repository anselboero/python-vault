import requests
from vault.error import ClientError

class Session:
    """Vault Session Constructor.
    vault_subdomain (str): The DNS of the Vault for which you want to generate a session.
    version (str): The Vault REST API version.
    username (str): The Vault user name.
    password (str): The Vault password
    """

    

    def __init__(
        self,
        vault_subdomain,
        version,
        username,
        password
    ):
        self.session = self._init_session()
        self.METHODS = {
            "get": self.session.get,
            "post": self.session.post,
            "delete": self.session.delete
        }
        self.session_id = None

        uri = f"https://{vault_subdomain}/api/v{version}/auth"

        data = {
            'username': username,
            'password': password
        }
        try: 
            response = self.send_request('post', uri, data=data)
        except Exception as e:
            raise e
        
        self._update_session_id(response['sessionId'])
        

        self.base_url = f'https://{self.vault_domain}/api/v{self.version}/'
        # Domain is the 
        self.domain = None
    

    def _init_session(self):
        """Initialize the Session"""
        headers = self._get_headers()
        session = requests.Session()
        session.headers.update(headers)

        return session
    
    def _get_headers(self):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        return headers

    def send_request(self, http_method, url_path, **kwargs):

        params = {
            'url': url_path,

        }
        params = params | kwargs

        response = self.METHODS[http_method](**params)
        self._handle_exception(response)
        return response.json()
    
    def _update_session_id(self, session_id):
        self.session_id = session_id
        self.session.headers.update({'Authorization': session_id})


    def _handle_exception(self, response):
        status_code = response.status_code
        if status_code == 200:
            data = response.json()
            if data['responseStatus'] == 'FAILURE':
                errors = data['errors']
                raise ClientError(status_code, errors )
