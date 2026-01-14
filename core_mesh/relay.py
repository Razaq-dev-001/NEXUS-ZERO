import socket

MY_IP = socket.gethostbyname(socket.gethostname())

def relay_message(message, target_ip, final_destination):
    """
    Simulates a 'Hop'. If this node is not the final destination, 
    it forwards the packet to the next peer.
    """
    if MY_IP == final_destination:
        print(f"✅ Message Received: {message}")
    else:
        print(f"🔄 Relaying message toward {final_destination} via {target_ip}...")
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((target_ip, 5006))
                s.sendall(f"{final_destination}|{message}".encode())
        except Exception as e:
            print(f"❌ Relay failed: {e}")

# Example usage for the demo
# relay_message("HELP: Sector 4", "192.168.1.15", "192.168.1.50")