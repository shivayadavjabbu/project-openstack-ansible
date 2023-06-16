def generate_keepalived_config(filename, interface, router_id, priority, auth_pass, virtual_ip_file):
    with open(virtual_ip_file, 'r') as f:
        virtual_ip = f.read().strip()

    config = f"""! Configuration File for keepalived

vrrp_instance VI_1 {{
    state MASTER
    interface {interface}
    virtual_router_id {router_id}
    priority {priority}
    advert_int 1
    authentication {{
        auth_type PASS
        auth_pass {auth_pass}
    }}
    virtual_ipaddress {{
        {virtual_ip}
    }}
}}"""

    with open(filename, 'w') as f:
        f.write(config)
    f.close()

# Example usage
generate_keepalived_config('./temp/keepalived.conf', 'ens3', 101, 100, '1111', './temp/haproxyfloating')
generate_keepalived_config('./temp/keepalivedbackup.conf', 'ens3', 101, 101, '1111','./temp/haproxyfloating')
