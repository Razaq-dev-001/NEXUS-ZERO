import socket
import threading
import time

class MeshDiscovery:
    def __init__(self, port=5005):
        self.port = port
        self.peers = set()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.socket.bind(('', self.port))

    def listen(self):
        """Listen for 'chirps' from other Nexus nodes."""
        print(f"📡 Listening for nearby Nexus nodes on port {self.port}...")
        while True:
            data, addr = self.socket.recvfrom(1024)
            if data == b"NEXUS_DISCOVERY":
                if addr[0] not in self.peers:
                    print(f"✨ New Node Discovered: {addr[0]}")
                    self.peers.add(addr[0])

    def broadcast(self):
        """Send out a 'chirp' every 5 seconds."""
        print("📢 Broadcasting presence to the mesh...")
        while True:
            self.socket.sendto(b"NEXUS_DISCOVERY", ('<broadcast>', self.port))
            time.sleep(5)

    def start(self):
        threading.Thread(target=self.listen, daemon=True).start()
        threading.Thread(target=self.broadcast, daemon=True).start()

if __name__ == "__main__":
    node = MeshDiscovery()
    node.start()
    while True: time.sleep(1) # Keep main thread alive