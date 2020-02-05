from twisted.internet.protocol import Protocol, Factory
from twisted.internet.endpoints import TCP4ClientEndpoint
from sys import stdout
from twisted.internet import reactor

host = 'localhost'
port = 8000

class Echo(Protocol):
    def dataReceived(self, data):
        print(data)
    def connectionMade(self):
        self.transport.write(input("Enter your name: ").encode('utf-8'))
        self.transport.loseConnection()

class EchoFactory(Factory): 
    
    def startedConnecting(self, connector):
        print('Started to connect.')

    def buildProtocol(self, addr):
        print('Connected.')
        return Echo()

    def clientConnectionLost(self, connector, reason):
        print('Lost connection.  Reason:', reason)

    def clientConnectionFailed(self, connector, reason):
        print('Connection failed. Reason:', reason)

if __name__ == "__main__":
    endpoint = TCP4ClientEndpoint(reactor, host, port)
    endpoint.connect((EchoFactory()))
    reactor.run()