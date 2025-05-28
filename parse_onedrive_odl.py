
import re
from pathlib import Path

def parse_odl_log(file_path):
    """Parse OneDrive .odl log file and extract useful entries."""
    pattern = re.compile(r'(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+Z).*?(?P<event>Uploading|Downloading|Synced|Deleted|Created).*?(?P<file_path>C:[^\s]+)', re.IGNORECASE)

    results = []

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            match = pattern.search(line)
            if match:
                results.append({
                    'timestamp': match.group('timestamp'),
                    'event': match.group('event'),
                    'file_path': match.group('file_path')
                })

    return results


if __name__ == "__main__":
    import argparse
    import csv

    parser = argparse.ArgumentParser(description="Parse OneDrive .odl log file")
    parser.add_argument("log_file", help="Path to the .odl log file")
    parser.add_argument("-o", "--output", help="CSV output file path", default="odl_log_parsed.csv")
    args = parser.parse_args()

    log_entries = parse_odl_log(args.log_file)

    if log_entries:
        with open(args.output, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['timestamp', 'event', 'file_path']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for entry in log_entries:
                writer.writerow(entry)

        print(f"Parsed {len(log_entries)} entries. Output saved to {args.output}")
    else:
        print("No matching log entries found.")
