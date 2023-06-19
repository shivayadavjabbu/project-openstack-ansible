def generate_keepalived_config(filename, interface, router_id, priority, auth_pass, virtual_ip,state):
    config = f"""! Configuration File for keepalived

vrrp_instance VI_1 {{
    state {state}
    interface {interface}
    virtual_router_id {router_id}
    priority {priority}
    advert_int 1
    virtual_ipaddress {{
        {virtual_ip}/32
    }}
}}"""

    with open(filename, 'w') as f:
        f.write(config)
    f.close()

# Example usage
generate_keepalived_config('./temp/keepalived.conf', 'ens3', 101, 101, '1111','192.168.0.4','MASTER')
generate_keepalived_config('./temp/keepalivedbackup.conf', 'ens3', 101, 100, '1111','192.168.0.4','BACKUP')
