#!/usr/bin/python3
"""
Log parsing with metrics computation
"""

import sys
import re

if __name__ == '__main__':

    line_count = 0
    total_file_size = 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {code: 0 for code in status_codes}

    def print_stats(stats: dict, total_size: int) -> None:
        print("File size:", total_size)
        for code in sorted(stats):
            if stats[code] > 0:
                print(code + ":", stats[code])

    try:
        for line in sys.stdin:
            line_count += 1
            line = line.strip()
            match = re.match(r'.*GET \/projects\/260 HTTP\/1\.1" (\d+) (\d+)', line)
            if match:
                status_code = match.group(1)
                file_size = int(match.group(2))
                if status_code in status_codes:
                    stats[status_code] += 1
                total_file_size += file_size
            if line_count % 10 == 0:
                print_stats(stats, total_file_size)
        print_stats(stats, total_file_size)
    except KeyboardInterrupt:
        print_stats(stats, total_file_size)
        raise