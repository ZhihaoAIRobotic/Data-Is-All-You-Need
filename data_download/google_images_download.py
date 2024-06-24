from googleapiclient.discovery import build
import requests
import os
from config import CONFIG


def google_image_search(query, api_key, cx, num_images=5):
    # Create a custom search service
    service = build("customsearch", "v1", developerKey=api_key)

    # Execute the search
    result = service.cse().list(q=query, cx=cx, searchType="image", num=num_images).execute()

    # Process and download images
    for i, item in enumerate(result.get("items", [])):
        image_url = item["link"]
        try:
            response = requests.get(image_url)
            if response.status_code == 200:
                # Create a directory for downloaded images if it doesn't exist
                if not os.path.exists("downloaded_images"):
                    os.makedirs("downloaded_images")
                
                # Save the image
                file_name = f"downloaded_images/image_{i+1}.jpg"
                with open(file_name, "wb") as file:
                    file.write(response.content)
                print(f"Downloaded: {file_name}")
            else:
                print(f"Failed to download image {i+1}")
        except Exception as e:
            print(f"Error downloading image {i+1}: {str(e)}")

if __name__ == "__main__":
    # Replace with your actual API key and Custom Search Engine ID
    API_KEY = CONFIG.search_engine_api_key
    CX = CONFIG.search_cx

    # Perform the search
    search_query = "cute puppies"
    google_image_search(search_query, API_KEY, CX)