"""
    Basic transaction
"""
import json
import hashlib

class transaction ():
    __attributes = [
        "issuer", "recipient", "amount", "hash", "signature"
    ]

    def __init__ (self, issuer="", recipient="", amount=0):
        self.issuer=issuer
        self.recipient=recipient
        self.amount=amount
        self.hash=None
        self.signature=None
        
    def toJson (self):
        "Return a Json encoded reprensentation of transaction"
        attrs={}
        attrs [attributeName] = self.getattr(attributeName) for attributeName in self.__attributes
        return json.dump(attrs, sort_keys=True)

    def sign(self, key):
        pass

    def compute_hash (self):
        """
            update hash of transaction
            :todo move to json representation instead of binary representation of object
        """
        self.hash = hashlib.sha256().upbate(bytes(self)).digest()
    
    def __getattribute__ (self, name):
        if name == "hash":
            if hash is None:
                self.compute_hash ()
        return object.__getattribute__(self, name)