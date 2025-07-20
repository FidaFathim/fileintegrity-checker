import os
import hashlib
import json
import argparse
from datetime import datetime

# Calculate SHA-256 hash of a file
def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except:
        return None

# Load hash database from JSON
def load_hash_db(db_file="hash_db.json"):
    if not os.path.exists(db_file):
        return {}
    with open(db_file, "r") as f:
        return json.load(f)

# Save hash database to JSON
def save_hash_db(data, db_file="hash_db.json"):
    with open(db_file, "w") as f:
        json.dump(data, f, indent=4)

# Scan directory and return dictionary of file paths and hashes
def scan_directory(directory):
    hash_data = {}
    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.abspath(os.path.join(root, file))
            file_hash = calculate_hash(full_path)
            if file_hash:
                hash_data[full_path] = file_hash
    return hash_data

# Compare current and stored hashes
def verify_integrity(directory, db_file="hash_db.json"):
    old_hashes = load_hash_db(db_file)
    new_hashes = scan_directory(directory)

    modified = []
    deleted = []
    new = []

    for path in old_hashes:
        if path not in new_hashes:
            deleted.append(path)
        elif old_hashes[path] != new_hashes[path]:
            modified.append(path)

    for path in new_hashes:
        if path not in old_hashes:
            new.append(path)

    return modified, deleted, new

# Log changes to log.txt
def log_results(modified, deleted, new, logfile="log.txt"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(logfile, "a") as log:
        log.write(f"\n--- Scan at {now} ---\n")
        for m in modified:
            log.write(f"[MODIFIED] {m}\n")
        for d in deleted:
            log.write(f"[DELETED]  {d}\n")
        for n in new:
            log.write(f"[NEW]      {n}\n")

# Command-line interface
def main():
    parser = argparse.ArgumentParser(description="🔐 File Integrity Checker")
    parser.add_argument("--scan", help="Directory to scan and store hashes")
    parser.add_argument("--verify", help="Directory to verify against hash database")
    parser.add_argument("--update", help="Directory to rescan and update hash database")
    args = parser.parse_args()

    if args.scan:
        data = scan_directory(args.scan)
        save_hash_db(data)
        print(f"[+] Scanned and saved hashes for {args.scan}")

    elif args.verify:
        modified, deleted, new = verify_integrity(args.verify)
        log_results(modified, deleted, new)
        print("[✓] Verification complete.")
        print(f"Modified files: {modified}")
        print(f"Deleted files: {deleted}")
        print(f"New files: {new}")
        print("Check log.txt for details.")

    elif args.update:
        data = scan_directory(args.update)
        save_hash_db(data)
        print(f"[+] Hash database updated for {args.update}")

    else:
        parser.print_help()

# ✅ Correct place to call main()
if __name__ == "__main__":
    main()
