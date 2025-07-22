# 🛡️ File Integrity Checker

A simple yet effective Python-based **File Integrity Checker** that helps detect unauthorized file changes (modifications, deletions, or additions) in a specified folder using **SHA-256 hashing**.

---

##  What It Does

- Scans a folder and generates hashes for all files.
- Saves the hashes to `data.csv`.
- On verification, compares current file states with the original hashes.
- Logs all changes (modified, deleted, and new files) to `log.txt`.

---

##  Folder Structure
fileintegrity-checker/
├── checker.py # Main script
├── data.csv # Stores original file hashes
├── log.txt # Stores verification results
├── test_folder/ # Sample folder with example files
│ ├── example.txt
│ └── demo.py



## 🚀 How to Use

1. **Clone the repo:**

```bash
git clone https://github.com/FidaFathim/fileintegrity-checker.git
cd fileintegrity-checker

##To scan a folder (initial hash generation):
python checker.py --scan test_folder

##To verify integrity (check for changes):
python checker.py --verify test_folder

📝 After verification, check log.txt for detailed output.

🛠️ Example Files Included

    example.txt — Sample text file.

    demo.py — Dummy Python script.

    You can modify these and run the --verify command to test the checker.

Why This Project?

This tool is a mini cybersecurity project designed for beginners and cybersecurity enthusiasts to understand how hashing can help maintain file integrity. It’s great for students, interns, and self-learners who want a hands-on idea for their GitHub portfolio.






