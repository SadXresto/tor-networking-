import requests
from bs4 import BeautifulSoup
import json
import time
import os

# Configuration
SURFACE_DOMAIN = "ahmia.fi"  # The public site to check for the .onion link
OUTPUT_FILE = "../data/ahmia_latest.json"  # Where to save the result (create this folder if missing)

def fetch_onion_link():
    print(f"Connecting to {SURFACE_DOMAIN}...")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(SURFACE_DOMAIN, headers=headers, timeout=15)
        
        # If the direct request fails with a proxy-like error or SSL issue in some environments, 
        # we might need to retry or handle specific errors gracefully.
        if response.status_code != 200:
            print(f"HTTP Error {response.status_code} received from {SURFACE_DOMAIN}")
            return None
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Common pattern: Ahmia stores the link as an <a href> tag containing .onion
        links_onion = soup.find_all('a', string=lambda text: text and '.onion' in text)
        
        if not links_onion:
             # Fallback search for common class patterns used by these sites (e.g., "hidden-service-url")
             hidden_links = soup.find_all(attrs={'class': lambda x: x and 'hidden' in str(x)}) 
             
             target_url = None
            
             if links_onion:
                 for i, link_tag in enumerate(links_onion):
                     href = link_tag.get('href') or ''
                     # Clean up the URL to be just the domain part usually
                     clean_domain = href.split('?')[0].split('/').pop() + '.onion'
                     
                     print(f"Found candidate at index {i}: https://{clean_domain}")
                     
                     # Heuristic check: Ahmia's main .onion is often very short (1-4 words) but let's stick to what's found.
                     target_url = "https://" + clean_domain 
                     break

             elif hidden_links:
                 for link in hidden_links:
                      text_content = ' '.join(link.stripped_strings)
                      if 'ahmia.onion' in text_content.lower():
                          parts = text_content.split('.')[-2]  # Rough extraction, usually simpler than full parse
                          # Better fallback: look for the specific domain string if it exists as a fragment
                           pass 

            else:
                print("No clear .onion URL pattern detected via standard tags.")


        return target_url

    except Exception as e:
        print(f"An error occurred during fetching: {e}")
        return None

def main():
    url = fetch_onion_link()
    
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    result = {
        "service": "Ahmia",
        "surface_domain": SURFACE_DOMAIN,
        "last_updated": time.strftime("%Y-%m-%d %H:%M:%S"),
        "url": url if url else null,
        "status": "active" if url else null
    }

    with open(OUTPUT_FILE, 'w') as f:
        json.dump(result, f, indent=4)

    print(f"\nResult saved to: {OUTPUT_FILE}")
    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()

