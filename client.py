import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

result = proxy.concatenate(s1, s2)

print("Concatenated String:", result)

#Python does not provide Java-style native RMI, so XML-RPC is used to implement equivalent remote method invocation.