import socket
import subprocess

def update_nginx_config(servers_count):
    config_path = '/etc/nginx/nginx.conf'
    # Define the new upstream block based on server count
    upstream_block = {
        1: 'server stk-server1:5001;',
        2: 'server stk-server1:5001;\n        server stk-server2:5002;',
        3: 'server stk-server1:5001;\n        server stk-server2:5002;\n        server stk-server3:5003;'
    }
    
    if servers_count not in upstream_block:
        raise ValueError("Invalid number of servers. Must be 1, 2, or 3.")
    
    # Read the existing nginx configuration
    with open(config_path, 'r') as file:
        config = file.read()

    # Replace the upstream block in the configuration
    new_upstream = f"""
    upstream stk_servers {{
        {upstream_block[servers_count]}
    }}
    """
    
    config = config.split("upstream stk_servers {")[0] + new_upstream + config.split("server {")[1]
    
    # Write the new configuration to the file
    with open(config_path, 'w') as file:
        file.write(config)
    
    # Reload NGINX to apply the new configuration
    subprocess.run(['nginx', '-s', 'reload'], check=True)

def start_ping_service():
    # Define the server and port for listening to pings
    server_address = ('0.0.0.0', 9999)
    
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind(server_address)
        print(f"Listening on {server_address}")
        
        while True:
            data, _ = sock.recvfrom(4096)
            message = data.decode().strip()
            
            try:
                servers_count = int(message)
                if servers_count in [1, 2, 3]:
                    update_nginx_config(servers_count)
                    print(f"Updated NGINX config for {servers_count} server(s).")
                else:
                    print(f"Invalid server count received: {servers_count}")
            except ValueError:
                print(f"Invalid message received: {message}")

if __name__ == "__main__":
    start_ping_service()
