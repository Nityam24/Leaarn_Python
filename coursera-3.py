# import re
# sum = 0

# file = open('Nirav-courseraData.py', 'r')
# for line in file:
#     numbers = re.findall('[0-9]+', line)
#     if not numbers:
#         continue
#     else:
#         for number in numbers:
#             sum += int(number)

# print(sum)


# import requests

# # Define the URL
# url = "http://data.pr4e.org/intro-short.txt"

# # Send an HTTP GET request to the URL
# response = requests.get(url)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Retrieve and print the HTTP headers
#     headers = response.headers
#     print("HTTP Response Headers:")
#     print("Last-Modified:", headers.get("Last-Modified"))
#     print("ETag:", headers.get("ETag"))
#     print("Content-Length:", headers.get("Content-Length"))
#     print("Cache-Control:", headers.get("Cache-Control"))
#     print("Content-Type:", headers.get("Content-Type"))
# else:
#     print("Failed to retrieve the URL. Status code:", response.status_code)

# import urllib.request
# from bs4 import BeautifulSoup

# # Input the URL of the actual data
# url = input("Enter the URL of the actual data: ")

# try:
#     # Open the URL and read its content
#     response = urllib.request.urlopen(url)
#     html = response.read()

#     # Parse the HTML using BeautifulSoup
#     soup = BeautifulSoup(html, 'html.parser')

#     # Find all <span> tags
#     span_tags = soup.find_all('span')

#     # Initialize variables to store count and sum
#     count = 0
#     total_sum = 0

#     # Loop through <span> tags
#     for tag in span_tags:
#         # Extract the text content of the <span> tag
#         content = tag.get_text()

#         # Convert the text content to an integer and add it to the total sum
#         total_sum += int(content)
#         count += 1

#     # Print the count and sum
#     print("Count", count)
#     print("Sum", total_sum)

# except Exception as e:
#     print("An error occurred:", str(e))



# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup

# def retrieve_last_name(url, position, count):
#     for i in range(count):
#         # Retrieve the web page
#         html = urllib.request.urlopen(url).read()
#         soup = BeautifulSoup(html, 'html.parser')

#         # Find all the anchor tags
#         tags = soup('a')

#         # Get the link at the specified position
#         link = tags[position - 1].get('href', None)
#         print("Retrieving:", link)

#         # Update the URL for the next iteration
#         url = link

#     # Extract the last name from the URL
#     last_name = urllib.parse.urlparse(url).path.split('_')[-1].split('.')[0]
#     return last_name

# # Input the starting URL, position, and count
# start_url = input("Enter URL: ")
# position = int(input("Enter position: "))
# count = int(input("Enter count: "))

# # Call the function to retrieve the last name
# last_name = retrieve_last_name(start_url, position, count)

# # Print the last name (name starts with "A")
# print("The answer to the assignment is:", last_name)



# import urllib.request
# import xml.etree.ElementTree as ET

# #Function to retrieve and parse XML data from a URL and compute the sum of comment counts
# def retrieve_and_compute_comment_sum(url):
#     try:
#         # Retrieve the XML data from the URL
#         response = urllib.request.urlopen(url)
#         data = response.read()

#         # Parse the XML data
#         tree = ET.fromstring(data)

#         # Find all 'count' elements using XPath
#         counts = tree.findall('.//count')

#         # Initialize variables for count and sum
#         count = 0
#         total_sum = 0

#         # Loop through the 'count' elements and compute the sum
#         for count_elem in counts:
#             total_sum += int(count_elem.text)
#             count += 1

#         return count, total_sum

#     except Exception as e:
#         print("An error occurred:", str(e))
#         return None, None

# # Input the URL
# url = input("Enter location: ")

# # Call the function to retrieve and compute the comment sum
# count, total_sum = retrieve_and_compute_comment_sum(url)

# if count is not None and total_sum is not None:
#     print("Retrieving", url)
#     print(f"Count: {count}")
#     print(f"Sum: {total_sum}")
# else:
#     print("Failed to retrieve data. Please check the URL.")


# import urllib.request
# import json

# # Function to retrieve and parse JSON data from a URL and compute the sum of comment counts
# def retrieve_and_compute_comment_sum(url):
#     try:
#         # Retrieve the JSON data from the URL
#         response = urllib.request.urlopen(url)
#         data = response.read().decode()

#         # Parse the JSON data
#         json_data = json.loads(data)

#         # Extract the 'comments' list
#         comments = json_data.get('comments', [])

#         # Initialize variables for count and sum
#         count = 0
#         total_sum = 0

#         # Loop through the 'comments' list and compute the sum
#         for comment in comments:
#             total_sum += int(comment.get('count', 0))
#             count += 1

#         return count, total_sum

#     except Exception as e:
#         print("An error occurred:", str(e))
#         return None, None

# # Input the URL
# url = input("Enter location: ")

# # Call the function to retrieve and compute the comment sum
# count, total_sum = retrieve_and_compute_comment_sum(url)

# if count is not None and total_sum is not None:
#     print("Retrieving", url)
#     print(f"Count: {count}")
#     print(f"Sum: {total_sum}")
# else:
#     print("Failed to retrieve data. Please check the URL.")


# import urllib.request, urllib.parse, urllib.error
# import json

# # Function to retrieve place_id for a location using the JSON API
# def retrieve_place_id(location):
#     base_url = "http://py4e-data.dr-chuck.net/json?"
#     params = {
#         "address": location,
#         "key": 42  # This is not a real key, but the autograder doesn't require a real key.
#     }

#     # Construct the URL with parameters
#     url = base_url + urllib.parse.urlencode(params)

#     try:
#         # Retrieve the JSON data from the URL
#         response = urllib.request.urlopen(url)
#         data = response.read().decode()

#         # Parse the JSON data
#         json_data = json.loads(data)

#         # Extract and return the first place_id
#         place_id = json_data.get('results', [])[0].get('place_id', None)
#         return place_id

#     except Exception as e:
#         print("An error occurred:", str(e))
#         return None

# # Input the location
# location = input("Enter location: ")

# # Call the function to retrieve the place_id
# place_id = retrieve_place_id(location)

# if place_id is not None:
#     print("Retrieving", location)
#     print("Place id", place_id)
# else:
#     print("Failed to retrieve place_id. Please check the location or API endpoint.")
# # import re

# # Function to extract numbers from a given text and return their sum
# def extract_and_sum_numbers(filename):
#     try:
#         with open(filename, 'r') as file:
#             text = file.read()
#             numbers = re.findall(r'[0-9]+', text)
#             numbers = [int(num) for num in numbers]
#             return sum(numbers)
#     except FileNotFoundError:
#         return None

# # Input the filename of the actual data file
# filename = input("Enter the filename of the actual data: ")

# # Calculate the sum of numbers and print the result
# result = extract_and_sum_numbers(filename)

# if result is not None:
#     print("The sum of numbers in the file is:", result)
# else:
#     print("File not found. Please make sure the file is in the correct location.")


import sqlite3
import re
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Counts (org TEXT, count INTEGER)''')

conn.commit()
filename = input('Enter file name: ')
if len(filename) < 1: filename = 'mbox.txt'

email_regex = re.compile(r'From \S+@(\S+)', re.IGNORECASE)

with open(filename, 'r') as file:
    for line in file:
        match = email_regex.match(line)
        if match:
            org = match.group(1)
            cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
            row = cur.fetchone()
            if row is None:
                cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
            else:
                cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

conn.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print('Counts:')
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
