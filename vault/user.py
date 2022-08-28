from vault.base import VaultObject

class User(VaultObject):
    """Class related to the User Object"""
    def __init__(
        self,
        user_name__v = None,
        user_first_name__v: str = None,
        user_last_name__v: str = None,
        user_email__v: str = None,
        user_timezone__v: str = None,
        user_locale__v: str = None,
        security_policy_id__v: str = None, # SecurityPolicy Object
        vault_id__v: list = None,
        created_date__v: str = None, # Date
        created_by__v: str = None,
        modified_date__v: str = None,
        modified_by__v: str = None,
        domain_id__v: str = None,
        domain_name__v: str = None,
        user_language__v: str = None,
        alias__v: str = None,
        user_title__v: str = None,
        office_phone__v: str = None,
        fax__v: str = None,
        mobile_phone__v: str = None,
        site__v: str = None,
        is_domain_admin__v: bool = None,
        active__v: bool = None,
        domain_active__v: bool = None,
        user_needs_to_change_password__v: bool = None,
        federated_id__v: str = None,
        salesforce_user_name__v: str = None,
        last_login__v:str = None,
        medidata_uuid__v: str = None,
        company__v: str = None,
        group_id__v: str = None,
        security_profile__v: str = None,
        license_type__v: str = None,
        id: str = None # Object: users, type: id
    ):
        if not (user_name__v or id):
            raise ValueError("User_name__v cannot be empty")
        
        self._user_name__v = user_name__v
        self._id = id

        self._user_first_name__v = user_first_name__v
        self._user_last_name__v = user_last_name__v
        self._user_email__v = user_email__v
        self._user_timezone__v = user_timezone__v
        self._user_locale__v = user_locale__v
        self._security_policy_id__v = security_policy_id__v
        self._vault_id__v = vault_id__v
        self._created_date__v = created_date__v
        self._created_by__v = created_by__v
        self._modified_date__v = modified_date__v
        self._modified_by__v = modified_by__v
        self._domain_id__v = domain_id__v
        self._user_language__v = user_language__v
        self._alias__v = alias__v
        self._user_title__v = user_title__v
        self._office_phone__v = office_phone__v
        self._fax__v: fax__v
        self._mobile_phone__v = mobile_phone__v
        self._site__v = site__v
        self._is_domain_admin__v = is_domain_admin__v
        self._active__v = active__v
        self._domain_active__v = domain_active__v
        self._user_needs_to_change_password__v = user_needs_to_change_password__v
        self._federated_id__v = federated_id__v
        self._salesforce_user_name__v = salesforce_user_name__v
        self._last_login__v = last_login__v
        self._medidata_uuid__v = medidata_uuid__v
        self._company__v = company__v
        self._group_id__v = group_id__v
        self._security_profile__v = security_profile__v
        self._license_type__v = license_type__v

        # is_initialized is used for allowing Lazy Loading
        if self._user_name__v:
            self._is_initialized = True
        else:
            self._is_initialized = False

    @property
    def user_name__v(self):
        return self._get_attribute(self._user_name__v)
    
    @property
    def user_first_name__v(self):
        return self._get_attribute(self._user_first_name__v)
    
    @property
    def user_last_name__v(self):
        return self._get_attribute(self._user_last_name__v)
    
    @property
    def user_email__v(self):
        return self._get_attribute(self.user_email__v)
    
    @property
    def user_timezone__v(self):
        return self._get_attribute(self._user_timezone__v)
    
    @property
    def user_locale__v(self):
        return self._get_attribute(self._user_locale__v)
    
    @property
    def is_domain_admin__v(self):
        return self._get_attribute(self._is_domain_admin__v)
    
    @property
    def active__v(self):
        return self._get_attribute(self._active__v)
    
    @property
    def domain_active__v(self):
        return self._get_attribute(self._domain_active__v)
    
    @property
    def security_policy_id__v(self):
        return self._get_attribute(self._security_policy_id__v)
    
    @property
    def user_needs_to_change_password__v(self):
        return self._get_attribute(self._user_needs_to_change_password__v)
    
    @property
    def created_date__v(self):
        return self._get_attribute(self._created_date__v)
    
    @property
    def created_by__v(self):
        return self._get_attribute(self._created_by__v)
    
    @property
    def modified_date__v(self):
        return self._get_attribute(self._modified_date__v)
    
    @property
    def modified_by__v(self):
        return self._get_attribute(self._modified_by__v)
    
    @property
    def domain_id__v(self):
        return self._get_attribute(self._domain_id__v)
    
    @property
    def domain_name__v(self):
        return self._get_attribute(self._domain_name__v)
    
    @property
    def vault_id__v(self):
        return self._get_attribute(self._vault_id__v)
    
    @property
    def last_login__v(self):
        return self._get_attribute(self._last_login__v)
    
    @property
    def user_language__v(self):
        return self._get_attribute(self._user_language__v)
    
    @property
    def group_id__v(self):
        return self._get_attribute(self._group_id__v)
    
    @property
    def security_policy_id__v(self):
        return self._get_attribute(self._security_policy_id__v)
    
    @property
    def license_type__v(self):
        return self._get_attribute(self._license_type__v)
    
    def _get_attribute(self, attribute):
        if self._is_initialized:
            return attribute
