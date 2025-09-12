import psutil

def check_processes():
    alerts = []
    for proc in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent']):
        try:
            info = proc.info
            if info['cpu_percent'] > 80:
                alerts.append(f"High CPU usage: {info['name']} (PID {info['pid']})")
            if info['name'] in ["nc", "netcat"]:  # suspicious processes
                alerts.append(f"Suspicious process detected: {info['name']} (PID {info['pid']})")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return alerts