"""Module containing Vault Exceptions"""

class InvalidVersion(Exception):
    """Raised when Version number is not supported or invalid"""
    def __init__(self, message: str):
        super().__init__(message)

class ClientError(Exception):
    """Raised when a call to Veeva returns FAILURE as responseStatus"""
    def __init__(self, json_response):
        message = f"""Got a Failure response from Veeva API call.
        response Message: {json_response['responseMessage']},
        errors: {json_response['errors']},
        error type: {json_response['errorType']}"""
        super().__init__(message)





