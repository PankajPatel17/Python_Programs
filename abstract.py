from abc import ABC , abstractmethod

class TRAI(ABC):
    @abstractmethod
    def postpaid_plain(self):
        pass

class airtel(TRAI):
    def postpaid_plain(self):
        print("postpaid_plain given by airtek is : ",99.99)

class vodafone(TRAI):
    def postpaid_plain(self):
        print("vodafone given by airtek is : ",89.99)

A1=airtel()
A1.postpaid_plain()

V1=vodafone()
V1.postpaid_plain()