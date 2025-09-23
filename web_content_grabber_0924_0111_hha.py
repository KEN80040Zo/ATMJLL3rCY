# 代码生成时间: 2025-09-24 01:11:37
import requests
from bs4 import BeautifulSoup
import sys

"""
A simple web content grabber using Python and Requests.
This script is designed to fetch the content of a web page and print it.

Usage:
    python web_content_grabber.py <URL>
"""

def fetch_web_page(url):
    """
    Fetches the content of a given web page.

    Args:
# 改进用户体验
        url (str): The URL of the web page to fetch.

    Returns:
        str: The HTML content of the page.

    Raises:
        requests.RequestException: If there's an issue with the request.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        return response.text
    except requests.RequestException as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)


def main(url):
    """
    Main function to print the content of the web page.

    Args:
        url (str): The URL of the web page to print.
# 改进用户体验
    """
    html_content = fetch_web_page(url)
    soup = BeautifulSoup(html_content, 'html.parser')
    print(soup.prettify())  # Print the HTML content in a pretty format

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python web_content_grabber.py <URL>")
        sys.exit(1)

    main(sys.argv[1])