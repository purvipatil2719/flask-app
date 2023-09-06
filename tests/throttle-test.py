import requests
import time

# Configure the API endpoint and throttle limit
upload_url = 'http://example.com/upload'  # Replace with your actual upload endpoint URL
throttle_limit = 5  # Adjust to your throttle limit

# Create a list of files to upload (you may need to prepare these files)
files_to_upload = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt', 'file6.txt']

# Make repeated requests to exceed the throttle limit
for i in range(throttle_limit + 1):
    # Simulate uploading a file (you may need to adjust this part)
    file_to_upload = files_to_upload[i % len(files_to_upload)]
    files = {'file': open(file_to_upload, 'rb')}  # Adjust the file field name if needed

    response = requests.post(upload_url, files=files)

    print(f'Response {i + 1}: Status Code - {response.status_code}')

    # Sleep for a short time to simulate a delay between requests
    time.sleep(1)  # Adjust the sleep duration as needed
