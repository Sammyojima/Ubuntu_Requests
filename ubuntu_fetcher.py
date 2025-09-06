import requests
import os
import hashlib
from urllib.parse import urlparse

def get_filename_from_url(url):
    """Extract filename from URL or generate a default one"""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename:  # If no filename in URL, generate one
        filename = "downloaded_image.jpg"
    return filename

def get_file_hash(filepath):
    """Return SHA256 hash of a file (for duplicate check)"""
    with open(filepath, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def fetch_image(url, folder="Fetched_Images"):
    """Download and save image from a URL with precautions"""
    try:
        # Make directory
        os.makedirs(folder, exist_ok=True)

        # Fetch with requests (streaming to avoid memory overload)
        response = requests.get(url, timeout=10, stream=True)
        response.raise_for_status()  # Raise error for bad status

        # Check content-type header (only allow images)
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped (Not an image): {url}")
            return

        # Extract filename
        filename = get_filename_from_url(url)
        filepath = os.path.join(folder, filename)

        # Avoid duplicates by comparing file hash
        if os.path.exists(filepath):
            old_hash = get_file_hash(filepath)
            new_hash = hashlib.sha256(response.content).hexdigest()
            if old_hash == new_hash:
                print(f"✗ Skipped duplicate: {filename}")
                return
            else:
                # If name clash but content differs → add suffix
                base, ext = os.path.splitext(filename)
                filename = f"{base}_new{ext}"
                filepath = os.path.join(folder, filename)

        # Save image in binary mode
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Ask for multiple URLs
    urls = input("Enter image URLs (comma-separated): ").split(",")

    for url in urls:
        url = url.strip()
        if url:
            fetch_image(url)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
