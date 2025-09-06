# Ubuntu_Requests

**"I am because we are." – Ubuntu Philosophy**

Ubuntu_Requests is a Python program that mindfully connects to the wider web community, fetches shared images, and organizes them for later appreciation.  
It emphasizes **community, respect, and sharing** in line with Ubuntu principles.

---

## ✨ Features
- ✅ Fetch images from one or multiple URLs  
- ✅ Automatically creates a `Fetched_Images` folder  
- ✅ Extracts filename from URL or generates one  
- ✅ Validates content type (downloads only images)  
- ✅ Prevents duplicate downloads (via file hash check)  
- ✅ Gracefully handles connection and network errors  

---

## 🛠️ Requirements
- Python 3.x  
- `requests` library  

Install requirements with:  
```bash
pip install requests

🌍 Ubuntu Principles in Action
Community → Connects to the wider web community
Respect → Handles errors gracefully without crashing
Sharing → Organizes images for later appreciation
Practicality → Provides a useful, real-world tool

🚀 Usage

Clone the repository:
git clone https://github.com/sammyojima/Ubuntu_Requests.git
cd Ubuntu_Requests

Run the script:
python ubuntu_fetcher.py

Enter one or multiple image URLs (comma-separated), for example:
https://linuxiac.com/wp-content/uploads/2020/06/ubuntu-linux.jpg), https://example.com/ubuntu2.png

Images will be saved in the Fetched_Images/ directory.

Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Enter image URLs (comma-separated): https://example.com/ubuntu-wallpaper.jpg
✓ Successfully fetched: ubuntu-wallpaper.jpg
✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg
Connection strengthened. Community enriched.


📜 License
This project is open source and available under the MIT License

"A person is a person through other persons." – Ubuntu Philosophy
