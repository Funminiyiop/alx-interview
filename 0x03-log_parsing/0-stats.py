#!/usr/bin/python3

"""
Write a script that reads stdin line by line and computes metrics:
"""

import sys


def printer(stats: dict, file_size: int) -> None:
    """ Function to print statistics """
    print("File size: {:d}".format(file_size))

    for k, v in sorted(stats.items()):
        if v:
            print("{}: {}".format(k, v))


def function() -> None:
    """ Stdin processing function """
    # Initialize variables for file size and line count
    line_count, file_size = 0, 0
    # List of status codes to track
    stat_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    # Dictionary to store count for each status code
    stat_count = {k: 0 for k in stat_codes}

    try:
        # Iterate through each line from stdin
        for line in sys.stdin:
            # Increment line count
            line_count += 1

            # Split the line by spaces into a list of words
            data = line.split()
            # print(data)

            try:
                # Attempt to extract the status code from the line
                # Position; before last
                status_code = data[-2]

                # If the status code is in the list; update count
                if status_code in stat_count:
                    stat_count[status_code] += 1
            except Exception:
                pass

            try:
                # Attempt to extract the file size from the line and
                # update total file size
                file_size += int(data[-1])
            except Exception:
                pass

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                # calling printer
                printer(stat_count, file_size)

        # Print final statistics
        printer(stat_count, file_size)

    except KeyboardInterrupt:
        # Handle keyboard interruption (Ctrl+C) and print final statistics
        printer(stat_count, file_size)
        raise


if __name__ == '__main__':
    """ Import control """
    function()