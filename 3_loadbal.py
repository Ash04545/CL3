# LoadBal Code ---------------------------------------------------

import random

class Server:
    def __init__(self, name):
        self.name = name
        self.active_connections = 0

    def handle_request(self):
        self.active_connections += 1

    def finish_request(self):
        if self.active_connections > 0:
            self.active_connections -= 1


class RoundRobinLoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def get_server(self):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server


servers = [Server(f"Server-{i}") for i in range(3)]
lb = RoundRobinLoadBalancer(servers)

for i in range(10):
    server = lb.get_server()
    server.handle_request()
    print(f"Request {i+1} assigned to {server.name}")

# Create Server -----------------------------------------------

servers = ["Server1", "Server2", "Server3"]

requests = int(input("Enter number of client requests: "))

for i in range(requests):
    assigned_server = servers[i % len(servers)]
    print(f"Request {i+1} assigned to {assigned_server}")
