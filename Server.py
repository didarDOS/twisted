from twisted.internet.protocol import Factory, Protocol

from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

class Echo(Protocol):
    def __init__(self, client):
        self.client = client
        self.state = "GETNAME"
    def dataReceived(self, name):
        if self.state == "GETNAME":
            self.registrate_client(name)
    def connectionMade(self):
        self.count = len(self.client)
        
        print("Was connected", self.count + 1, "clients")

        self.transport.write(b"Welcome! There are currently %d open connections.\n" %
                                self.count)
        print(self.client, )
    def registrate_client(self, name):  
        self.name = name 
        self.client[name] = self.name

class EchoFactory(Factory):

    def __init__(self):
        self.client = {}
    def buildProtocol(self, addr):
        return Echo(self.client)

if __name__ == "__main__":

    endpoint = TCP4ServerEndpoint(reactor, 8000)
    endpoint.listen(EchoFactory())
    reactor.run()