#!/usr/bin/env python3

import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'

def retrieve_events(url: str):
	"""gets data from url"""
	response = requests.get(url).text
	list = json.loads(response)
	return list

def print_events(events, n=5):
	"""prints events"""
	for x in events[:n]:
    		event = x['type'] + ' :: ' + x['repo']['name']
    		print(event)

def main():
	print(GHUSER)
	print(url)
	ret = retrieve_events(url)
	print_events(ret)

if __name__ == "__main__":
    main()
