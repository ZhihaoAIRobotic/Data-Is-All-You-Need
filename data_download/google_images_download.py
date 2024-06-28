from googleapiclient.discovery import build
import requests
import os
from config import CONFIG


def google_image_search(query, api_key, cx, num_images=5, download_path="downloaded_images"):
    if download_path[-1] != "/":
        download_path += "/"
    # Create a custom search service
    image_name_prefix = query.replace(" ", "_")
    service = build("customsearch", "v1", developerKey=api_key)
    if num_images < 10:
        # Execute the search
        result = service.cse().list(q=query, cx=cx, searchType="image", num=num_images).execute()
    
        # Process and download images
        for i, item in enumerate(result.get("items", [])):
            image_url = item["link"]
            try:
                response = requests.get(image_url)
                if response.status_code == 200:
                    # Create a directory for downloaded images if it doesn't exist
                    if not os.path.exists(download_path):
                        os.makedirs(download_path)           
                    # Save the image
                    file_name = download_path + image_name_prefix + f"image_{i+1}.jpg"
                    with open(file_name, "wb") as file:
                        file.write(response.content)
                    print(f"Downloaded: {file_name}")
                else:
                    print(f"Failed to download image {i+1}")
            except Exception as e:
                print(f"Error downloading image {i+1}: {str(e)}")
    if num_images >= 10:
        for i in range(1, num_images+1, 10):
            if i + 10 > num_images:
                result = service.cse().list(q=query, cx=cx, searchType="image", num=num_images-i+1, start=i).execute()
            else:
                result = service.cse().list(q=query, cx=cx, searchType="image", num=10, start=i).execute()
            for j, item in enumerate(result.get("items", [])):
                image_url = item["link"]
                try:
                    response = requests.get(image_url)
                    if response.status_code == 200:
                        # Create a directory for downloaded images if it doesn't exist
                        if not os.path.exists(download_path):
                            os.makedirs(download_path)
                        
                        # Save the image
                        file_name = download_path + image_name_prefix + f"image_{i+j}.jpg"
                        with open(file_name, "wb") as file:
                            file.write(response.content)
                        print(f"Downloaded: {file_name}")
                    else:
                        print(f"Failed to download image {i+j}")
                except Exception as e:
                    print(f"Error downloading image {i+j}: {str(e)}")

if __name__ == "__main__":
    # Replace with your actual API key and Custom Search Engine ID
    API_KEY = CONFIG.search_engine_api_key
    CX = CONFIG.search_cx

    # Perform the search
    search_query = "spilled coffee"
    google_image_search(search_query, API_KEY, CX, num_images=12, download_path="data/downloaded_images")
