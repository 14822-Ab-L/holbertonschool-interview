#!/usr/bin/python3
"""Reads stdin lines and computes metrics"""
import sys


def print_stats(total_size, status_codes):
    """Print the current statistics."""
    print("File size: {}".format(total_size))

    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


def main():
    """Read log lines and calculate statistics."""
    total_size = 0
    line_count = 0
    valid_codes = {200, 301, 400, 401, 403, 404, 405, 500}
    status_codes = {}

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            try:
                if len(parts) < 2:
                    raise ValueError

                file_size = int(parts[-1])
                status_code = int(parts[-2])

                if status_code not in valid_codes:
                    raise ValueError

                total_size += file_size
                status_codes[status_code] = (
                    status_codes.get(status_code, 0) + 1
                )

            except (ValueError, IndexError):
                pass

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        pass
    finally:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
