import requests
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

# Bitbucket API details
API_TOKEN = "ATCTT3xFfGN0qqXFhBtt2nSujtXayKSZYp9KirKJGDkqIT9lb0E_IUKqi3ujwDfJejdEtGX95ruIWNK4lnW4y9lJhnylDUdshTA_6VKdjfDnDiLRqnTFIiaW2w8hF93_ebOWwuRoEdlvExh0plyi3W-WfPMULlESIBIISjK_lLNJ6MQRO5Vwg_M=B19DA4CD"
WORKSPACE = "maintainer-test"
REPO_SLUG = javaproject_maintainer
PR_NUMBER = 3  # Change to a valid PR number

# API URL
PR_INFO_URL = f"https://api.bitbucket.org/2.0/repositories/{WORKSPACE}/{REPO_SLUG}/pullrequests/{PR_NUMBER}"
COMMENT_URL = f"https://api.bitbucket.org/2.0/repositories/{WORKSPACE}/{REPO_SLUG}/pullrequests/{PR_NUMBER}/comments"
GET_REPO_URL = f"https://api.bitbucket.org/2.0/repositories/bitoai/cra-test"
UPDATE_POST_COMMENT = f"https://api.bitbucket.org/2.0/repositories/bitoai/akash-test/pullrequests/1/comments/606854500"

# Headers for authentication
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Accept": "application/json"
}

def make_request(max_retries=5):
    """Function to send a request to Bitbucket and check rate limits."""
    retry_count = 0
    backoff_time = 0.02  # Initial backoff time in seconds
    
    while retry_count < max_retries:
        response = requests.get(PR_INFO_URL, headers=HEADERS)
        if response.status_code == 200:
            print("Success")
            return response
        else:
            print("Error")

        print("Request Completed")
        if response.status_code == 429:
            print(f"Rate limit hit, backing off for {backoff_time} seconds")
            time.sleep(backoff_time)
            backoff_time *= 2  # Exponential backoff
            retry_count += 1
        else:
            time.sleep(0.02)  # Short sleep for non-rate-limit errors
    
    return None  # Return None if max retries exceeded

def trigger_rate_limit(thread_count=100):
    """Launch multiple threads to exhaust Bitbucket's rate limit."""
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        futures = [executor.submit(make_request) for _ in range(thread_count)]
        for future in as_completed(futures):
            future.result()  # Wait for all threads to complete

if __name__ == "__main__":
    trigger_rate_limit(thread_count=20)  # Adjust thread count as needed
