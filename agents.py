
from detectors.process import check_processes
from detectors.network import check_network
from detectors.file_integrity import init_baseline, check_files
import time

def main():
    init_baseline()
    print("🔐 Endpoint Detector started...")
    while True:
        alerts = []
        alerts.extend(check_processes())
        alerts.extend(check_network())
        alerts.extend(check_files())

        if alerts:
            print("⚠️ Alerts:")
            for a in alerts:
                print(" -", a)

        time.sleep(10)  # run every 10s

if __name__ == "__main__":
    main()