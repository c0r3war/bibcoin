"""
    All about blockchain
"""

from datetime import datetime
import hashlib

class Block:
    "A basic block of blockchain"

    def __init__(self, prevblock=None):
        self.transactions = []
        self.prevblock = prevblock
        self.timestamp = datetime.utcnow()
        self.nounce = 0
        self.hash = None
    #
    # Private methods
    #
    def _hashTransactions(self):
        globalHash = hashlib.sha256()
        for transaction in self.transactions:
            theHash = transaction.hash if hasattr (transaction,"hash") else hashlib.sha256 ().update (bytes (transaction)).digest ()
            globalHash.update (theHash)
        return globalHash.digest ()
    
    def mine (self):
        """
            Basic mining function (an infinite loop that iterate a nounce in order to generate a SHA256 hash; loop ends when the hash
            starts with '0')
        """
        TransactionsHash = self._hashTransactions ()
        HeaderHash = hashlib.sha256 ()
        HeaderHash.update (bytes(self.prevblock)).update(bytes(selftimestamp)).update(bytes(TransactionsHash))
        for nounce in range (0,None,1)
            tempHash = HeaderHash.copy()
            tempHash.update (bytes(nounce))
            blockHash = tempHash.digest ()
            if blockHash.startsWith (b'0'):
                self.nounce  = nounce
                self.hash = blockHash
                exit

        