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
        self.nounce = 0
        self.hash = None
        self.height = 0

        # If preblock == None, then this is the first block of the chain, initialisze it as block 0
        if prevblock is None:
            self.timestamp = datetime(1974, 8, 18)
            self.transactions.append(new transaction ("god", "me", 100))
        else:
            self.timestamp = datetime.utcnow()
    #
    # Private methods
    #
    def _hashTransactions(self):
        globalHash = hashlib.sha256()
        for transaction in self.transactions:
            # @todo: implement a hsh method in block with caching
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

        