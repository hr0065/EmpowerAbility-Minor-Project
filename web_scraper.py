# import requests
# from bs4 import BeautifulSoup

# # Define the URL of the job portal you want to scrape
# url = 'https://example.com/job-listings'

# # Send an HTTP GET request to the URL
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the HTML content of the page using BeautifulSoup
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Identify the HTML elements that contain job listings
#     job_listings = soup.find_all('div', class_='job-listing')

#     # Iterate through the job listings and extract relevant information
#     for job in job_listings:
#         title = job.find('h2', class='job-title').text
#         company = job.find('p', class='company-name').text
#         location = job.find('p', class='job-location').text
#         description = job.find('p', class='job-description').text

#         # You can choose to print or store this information as needed
#         print(f'Title: {title}')
#         print(f'Company: {company}')
#         print(f'Location: {location}')
#         print(f'Description: {description}')
#         print('\n')

# else:
#     print('Failed to retrieve the page. Status code:', response.status_code)
