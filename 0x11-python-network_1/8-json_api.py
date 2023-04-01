#!/usr/bin/env python3
"""
Takes in a letter and sends a POST request to a search endpoint
with the letter as a parameter.
"""
if __name__ == '__main__':
    import requests
    from sys import argv

    if len(argv) == 2:
        query = argv[1]
    else:
        query = ""

    url = 'http://example.com/search'  # replace with your endpoint URL
    try:
        response = requests.post(url, data={'q': query})
        response.raise_for_status()  # raise an exception if the request failed

        data = response.json()
        result_id = data.get('id')
        result_name = data.get('name')

        if not data or not result_id or not result_name:
            print("No result")
        else:
            print(f"[{result_id}] {result_name}")
    except (requests.exceptions.RequestException, ValueError):
        print("Could not retrieve search results.")


