import hashlib
import os

def hash_file(path):
    sha256 = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

# Initial baseline
BASELINE = {
    "/etc/passwd": None
}

def init_baseline():
    for f in BASELINE.keys():
        if os.path.exists(f):
            BASELINE[f] = hash_file(f)

def check_files():
    alerts = []
    for f, old_hash in BASELINE.items():
        if os.path.exists(f):
            new_hash = hash_file(f)
            if old_hash and new_hash != old_hash:
                alerts.append(f"File modified: {f}")
    return alerts