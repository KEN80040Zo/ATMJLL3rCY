# 代码生成时间: 2025-09-22 18:19:09
import requests
from requests.exceptions import HTTPError

"""
Theme Switcher Service
This script provides a simple theme switching functionality by making HTTP requests to a specified API.

Attributes:
    None

Methods:
    switch_theme(user_id, theme): Switches the theme for a given user.
"""

class ThemeSwitcherService:
    def __init__(self, api_url):
        """
        Initializes the ThemeSwitcherService with the API URL.
        
        Args:
            api_url (str): The base URL of the API that handles theme switching.
        """
        self.api_url = api_url

    def switch_theme(self, user_id, theme):
        """
        Switches the theme for a given user.
        
        Args:
            user_id (str): The ID of the user whose theme is to be switched.
            theme (str): The theme to switch to.
        
        Returns:
            dict: The response from the API.
        
        Raises:
            HTTPError: If the HTTP request returns an unsuccessful status code.
        """
        # Construct the endpoint URL with the user ID
        endpoint_url = f"{self.api_url}/switch_theme/{user_id}"
        
        # Prepare the payload with the theme information
        payload = {"theme": theme}
        
        try:
            # Make a POST request to the API endpoint
            response = requests.post(endpoint_url, json=payload)
            response.raise_for_status()  # Raise an HTTPError for bad responses
        except HTTPError as http_err:
            # Handle HTTP errors
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            # Handle other possible errors
            print(f"An error occurred: {err}")
            raise
        else:
            # Return the JSON response from the API
            return response.json()

# Example usage
if __name__ == '__main__':
    api_url = "https://example.com/api"  # Replace with the actual API URL
    user_id = "12345"  # Replace with the actual user ID
    theme = "dark"  # Replace with the desired theme
    
    theme_switcher = ThemeSwitcherService(api_url)
    try:
        result = theme_switcher.switch_theme(user_id, theme)
        print("Theme switched successfully!")
        print(result)
    except Exception as e:
        print(f"An error occurred while switching the theme: {e}")