Wisconsin Supper Clubs Data Collection Project
===========================================

Description
-----------
This project collects and geocodes Wisconsin supper club locations using Google Maps API. The data collection includes information such as names, addresses, and geographical coordinates of supper clubs across Wisconsin.

Project Structure
---------------
.idea/              - PyCharm project settings
data/               - Collected and processed data
beautifulsoup.py    - Web scraping script
geocoding-api-test.ipynb    - Jupyter notebook for testing geocoding
wi-supper-club-collector.ipynb    - Main data collection notebook

Setup
-----
1. Clone the repository
2. Create a .env file based on .env.example
3. Add your Google Maps API key to .env


Environment Variables
------------------
Required environment variables in .env:
- GOOGLE_MAPS_API_KEY: Your Google Maps API key

Data Collection
-------------
The project collects the following data for each supper club:
- Name
- Address
- City
- State
- ZIP code
- Region
- Website
- Phone number
- Geographical coordinates (latitude/longitude)

Usage
-----
1. Run wi-supper-club-collector.ipynb to collect basic data
2. Run geocoding-api-test.ipynb for a simple test for an address input
3. Processed data will be saved in the data/ directory

Note
----
Please ensure your Google Maps API key is kept secret and never committed to the repository.

Author
------
Yu-Ning Liu (GitHub: tooobening)

Last Updated
-----------
November 2024