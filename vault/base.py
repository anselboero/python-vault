class VaultObject():
    """Base Class for Vault Objects"""
    
    @classmethod
    def de_json(cls, data):
        """Convert JSON Data to a Vault Object"""
        return cls(**data)

