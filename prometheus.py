def generate_prometheus_config():
    with open('server.conf', 'r') as server_file:
        num_servers = int(server_file.read().strip())

    config = f"""
global:
  scrape_interval: 5s

scrape_configs:
  - job_name: 'bastion_node'
    static_configs:
      - targets: ['192.168.0.10:9090']
  - job_name: 'proxy_node'
    static_configs:
      - targets: ['192.168.0.11:9100', '192.168.0.12:9100']
      
  - job_name: 'backend_servers'
    static_configs:  
""" 

    # Generate the targets based on the number of servers
    for i in range(num_servers):
        ip_address = f"192.168.0.{21 + i}:9100"
        if num_servers == 1:
            config += f"      - targets: ['{ip_address}']\n"
        else:
            if i == 0:
                config += f"      - targets: ['{ip_address}',"
            elif i == num_servers - 1:
                config += f" '{ip_address}']\n"
            else:
                config += f" '{ip_address}',"
    return config

def write_prometheus_config():
    config = generate_prometheus_config()
    with open('./temp/prometheus.yml', 'w') as file:
        file.write(config)
    file.close()

write_prometheus_config()

