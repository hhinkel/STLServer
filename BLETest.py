from bluetooth import *

def inputAndSend():
    print("\nType somethings\n")
    while True:
        data = input()
        if len(data) == 0:
            break
        sock.send(data)
        sock.send("\n")
        
def rxAndEcho():
    sock.send("\nSend anything\n")
    while True:
        data = sock.recv(buf_size)
        if data:
            print(data)
            sock.send(data)
            
    
#MAC address of ESP32
addr =  "60:55:F9:20:A6:86"
uuid = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
service_matches = find_service(uuid = uuid, address = addr)
#service_matches = find_service(address = addr)

buf_size = 1024

if len(service_matches) == 0:
    print("Could not find the SampleServer service")
    sys.exit(0)
    
for s in range(len(service_matches)):
    print("\nservice_matches: [" + str(s) + "]:")
    print(service_matches[s])

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

port = 1
print("Connecting to \"%s\" on %s, port %s" % (name, host, port))

#Create the client socket
sock = BLuetoothSocket(RFCOMM)
sock.connect((host, port))

print("Connected")

inputAndSend()
# rxAndEcho()

sock.close()
print("Bye")
