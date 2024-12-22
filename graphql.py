import requests
from internal.utils.save_to_json import save_to_json

# Define the URL
url = "https://gql.tokopedia.com/graphql/SearchProductV5Query"

# Define the headers
headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "bd-device-id": "7443002904782816775",
    "content-type": "application/json",
    "cookie": "_UUID_NONLOGIN_=efc4cada836a20c977fe35ecdb5f1a55; DID_JS=NzAwZDU1ZTEyM2IyMjIwNzlmNzJlMzFiYWEyMjJkNzU3MDZlODcxZTA5NmI1ZTc1ZDExM2UxM2Q4YjQ5ZmY2MmNlMzA0MzllMzI4ZjUxNGFmMWZkMWZhNjk2MWM5YmZi47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=; _SID_Tokopedia_=mi0ET-aeVsttIL1FJ63CNIR1NRVNC8BxJ36w-qN_y-uS4WRtXo6Em4rMBKFBHQAdIOzl2uUJYnSPxlL1osalEPFhYdM2AoxyTt9lFkKxbe_wpoOSlbAmnpXAOiBbltdN",
    "iris_session_id": "",
    "origin": "https://www.tokopedia.com",
    "priority": "u=1, i",
    "referer": "https://www.tokopedia.com/search?q=asus%20rog",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "tkpd-userid": "0",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "x-dark-mode": "false",
    "x-device": "desktop-0.0",
    "x-price-center": "true",
    "x-source": "tokopedia-lite",
    "x-tkpd-lite-service": "zeus",
}
pagination = 1
size = 200
keyword = "asus rog"
# Define the payload (data)
data = [
    {
        "operationName": "SearchProductV5Query",
        "variables": {
            "params": f"device=desktop&l_name=sre&ob=23&page={pagination}&q={keyword}&related=true&rows={size}&safe_search=false&scheme=https&shipping=&show_adult=false&source=search&st=product&start=0&topads_bucket=true&unique_id=efc4cada836a20c977fe35ecdb5f1a55&user_id=0&variants="
        },
        "query": """
        query SearchProductV5Query($params: String!) {
          searchProductV5(params: $params) {
            data {
              products {
                name
                url
                price {
                  number
                }
                shop {
                  name
                  city
                }
              }
            }
          }
        }
        """,
    }
]

# Send the POST request
response = requests.post(url, headers=headers, json=data)

# Print the response
if response.status_code == 200:
    print("Response JSON:")
    save_to_json(data=response.json(), filename="extracted_using_graphql")
    
    # print(json.dumps(response.json(), indent=4))
else:
    print(f"Error: {response.status_code}")
    print(response.text)
