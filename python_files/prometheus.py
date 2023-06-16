def generate_prometheus_config():
    with open('./temp/fixedip', 'r') as ip_file:
        ip_addresess = ip_file.read().splitlines()
    config = f"""
global:
  scrape_interval: 5s

scrape_configs:
  - job_name: 'bastion_node'
    static_configs:
      - targets: ['192.168.0.10:9090']
  - job_name: 'front_endservers--haproxy'
    static_configs:
      - targets: ['192.168.0.11:9100', '192.168.0.12:9100']
      
  - job_name: 'backend_servers'
    static_configs:  
""" 

    # Generate the targets based on the number of servers
    for i in range(0,len(ip_addresess)):
        ip_address = ip_addresess[i]
        ip_address = f"{ip_address}:9100"
        if len(ip_addresess) == 1:
            config += f"      - targets: ['{ip_address}']\n"
        else:
            if i == 0:
                config += f"      - targets: ['{ip_address}',"
            elif i == len(ip_addresess) - 1:
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

