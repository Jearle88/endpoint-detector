import psutil

def check_network():
    alerts = []
    for conn in psutil.net_connections(kind='inet'):
        if conn.status == 'LISTEN':
            laddr = f"{conn.laddr.ip}:{conn.laddr.port}"
            if conn.laddr.port not in [22, 80, 443]:  # whitelist common ports
                alerts.append(f"Unexpected open port: {laddr}")
    return alerts
