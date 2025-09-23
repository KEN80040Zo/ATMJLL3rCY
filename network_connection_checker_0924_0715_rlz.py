# 代码生成时间: 2025-09-24 07:15:56
import requests
import json

"""
A network connection status checker using the requests library in Python.
This script attempts to connect to a predefined list of URLs to check if the network connection is working.
"""

def check_connection(url):
    """
    Checks if a single URL is reachable.
    :param url: The URL to check.
    :return: Tuple of boolean indicating connection status and the status code of the response.
    """
    try:
        response = requests.get(url, timeout=5)  # Set a 5-second timeout
        return True, response.status_code
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False, None

def main():
    """
    Main function that checks the network connection to a list of URLs and prints the results.
    """
    # List of URLs to check
    urls = [
        "https://www.google.com",
        "https://www.github.com",
        "https://www.google.com.hk"
    ]

    results = {}
    for url in urls:
        status, code = check_connection(url)
        results[url] = {
            'status': 'connected' if status else 'not connected',
            'status_code': code
        }

    # Print the results
    print(json.dumps(results, indent=4))

if __name__ == '__main__':
    main()