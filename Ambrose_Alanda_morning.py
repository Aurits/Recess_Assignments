"""
from bs4 import BeautifulSoup
import requests

url = 'https://xeno-canto.org/'
response = requests.get(url)

# Get the title of the website

soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find('title')

print(title)

"""



"""
Assignment A12
Extraxt all bird species from the website url and generate the csv file or JSON format for the bird species, family and more
Extract all bird songs from this website url 
Use the API to get data  from the endpoint 


The endpoint for the webservice is at https://xeno-canto.org/api/2/recordings.
"""





"""

import requests
import csv

url = "https://xeno-canto.org/api/2/recordings?query=sp&species=true"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if "recordings" in data:
        species_list_with_duplicates = [recording["sp"] for recording in data["recordings"]]
        species_list_unique = list({recording["sp"] for recording in data["recordings"]})

        # Save the species_list_with_duplicates to list1.csv
        with open("list1.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Species"])  # Write header row
            writer.writerows([[species] for species in species_list_with_duplicates])  # Write species names row by row

        # Save the species_list_unique to list2.csv
        with open("list2.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Species"])  # Write header row
            writer.writerows([[species] for species in species_list_unique])  # Write species names row by row

        print("Data saved to CSV files successfully.")
else:
    print("Error: Unable to fetch data from the API.")
"""







""""
import requests
from bs4 import BeautifulSoup
import json

url = "https://xeno-canto.org/api/2/recordings?query=sp&species=true"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if "recordings" in data:
        species_list_with_duplicates = [recording["sp"] for recording in data["recordings"]]
        species_list_unique = list({recording["sp"] for recording in data["recordings"]})

        # Convert species lists to dictionaries for JSON serialization
        result_with_duplicates = {"species_with_duplicates": species_list_with_duplicates}
        result_unique = {"species_unique": species_list_unique}

        # Convert dictionaries to JSON format
        json_result_with_duplicates = json.dumps(result_with_duplicates)
        json_result_unique = json.dumps(result_unique)

        # Print JSON results
        print(json_result_with_duplicates)
        print(json_result_unique)
else:
    print("Error: Unable to fetch data from the API.")
"""



"""
import requests
import csv
import json

# URL of the Xeno-Canto API to fetch bird songs
url = "https://xeno-canto.org/api/2/recordings?query=sp&species=true"

# Send an HTTP GET request to the API and get the JSON response
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if "recordings" in data:
        bird_songs = []
        for recording in data["recordings"]:
            species = recording["sp"]
            family = recording.get("gen", "")  # Some recordings may not have the "gen" attribute
            country = recording.get("cnt", "")
            latitude = recording.get("lat", "")
            longitude = recording.get("lng", "")
            song_url = recording["file"]  # URL to the bird song

            # Store the extracted data in a Python dictionary
            bird_song = {
                "species": species,
                "family": family,
                "country": country,
                "latitude": latitude,
                "longitude": longitude,
                "song_url": song_url,
            }
            bird_songs.append(bird_song)

        # Convert the list of dictionaries to JSON
        json_data = json.dumps(bird_songs, indent=2)

        # Save the JSON data to a file
        with open("bird_songs.json", "w") as json_file:
            json_file.write(json_data)

        # Save the data to a CSV file
        csv_file_path = "bird_songs.csv"
        with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["species", "family", "country", "latitude", "longitude", "song_url"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(bird_songs)

        print("Data extracted and saved successfully.")
    else:
        print("No bird songs found in the API response.")
else:
    print(f"Error: Unable to fetch data from the API. Status Code: {response.status_code}")

"""



print("WARNING\nWARNING\nThis script will download 100 files of the songs to your machine!!!! ENJOY")



import requests
import os
import zipfile

# URL of the Xeno-Canto API to fetch bird songs
url = "https://xeno-canto.org/api/2/recordings?query=sp&species=true"

# Send an HTTP GET request to the API and get the JSON response
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if "recordings" in data:
        bird_songs = data["recordings"][:100]  # Get the first 100 bird songs

        # Create a folder to store the downloaded songs
        download_folder = "bird_songs"
        os.makedirs(download_folder, exist_ok=True)

        # Download the first 100 songs and save them
        for recording in bird_songs:
            song_url = recording["file"]
            song_filename = os.path.join(download_folder, os.path.basename(song_url))
            response = requests.get(song_url)
            if response.status_code == 200:
                with open(song_filename, "wb") as song_file:
                    song_file.write(response.content)

        # Create a zip file and add the downloaded songs to it
        zip_filename = "bird_songs.zip"
        with zipfile.ZipFile(zip_filename, "w") as zip_file:
            for recording in bird_songs:
                song_url = recording["file"]
                song_filename = os.path.join(download_folder, os.path.basename(song_url))
                zip_file.write(song_filename, os.path.basename(song_url))

        print("First 100 bird songs downloaded and saved to a zip file.")
    else:
        print("No bird songs found in the API response.")
else:
    print(f"Error: Unable to fetch data from the API. Status Code: {response.status_code}")

