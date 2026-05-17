import requests
import json
from typing import Dict, Any


def fetch_api_data(url: str) -> Dict[str, Any]:
    """
    Fetches data from REST API with full error handling.
    """
    try:
        print(f"🔄 Fetching data from: {url}")
        print("-" * 60)

        # Make GET request
        response = requests.get(url, timeout=10)

        # Check status code
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Success! Status: {response.status_code}")
            print(f"📊 Response size: {len(response.text)} characters")
            return data
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            print(f"Response: {response.text[:200]}...")
            return {}

    except requests.exceptions.Timeout:
        print("❌ ERROR: Request timed out (10s)")
    except requests.exceptions.ConnectionError:
        print("❌ ERROR: No internet connection")
    except requests.exceptions.RequestException as e:
        print(f"❌ Network Error: {str(e)}")
    except json.JSONDecodeError:
        print("❌ ERROR: Invalid JSON response")
        print(f"Raw response: {response.text[:200]}...")
    except Exception as e:
        print(f"❌ Unexpected Error: {str(e)}")

    return {}


def display_data_pretty(data: Dict[str, Any]):
    """
    Displays API data in beautiful format.
    """
    if not data:
        print("⚠️ No data to display")
        return

    print("\n" + "=" * 60)
    print("📋 API DATA (Pretty Printed):")
    print("=" * 60)

    # Pretty print JSON
    print(json.dumps(data, indent=2, ensure_ascii=False))

    # Show data summary
    print("\n📈 DATA SUMMARY:")
    print(f"   • Total keys: {len(data)}")
    if isinstance(data, (list, dict)):
        print(f"   • Type: {type(data).__name__}")
        if isinstance(data, list):
            print(f"   • Items: {len(data)}")


def demo_apis():
    """
    Test with popular free APIs.
    """
    apis = {
        "1": ("JSONPlaceholder Users", "https://jsonplaceholder.typicode.com/users"),
        "2": ("JSONPlaceholder Posts", "https://jsonplaceholder.typicode.com/posts/1"),
        "3": ("Joke API", "https://official-joke-api.appspot.com/random_joke"),
        "4": ("Cat Facts", "https://catfact.ninja/fact"),
        "5": ("Custom input", "")
    }

    print("🌐 POPULAR FREE APIs FOR TESTING:")
    print("-" * 40)
    for key, (name, url) in apis.items():
        print(f"{key}. {name}")

    choice = input("\n🎯 Choose API (1-5) or Enter custom URL: ").strip()

    if choice == "5":
        url = input("Enter API URL: ").strip()
    else:
        url = apis.get(choice, apis["1"])[1]

    if url:
        data = fetch_api_data(url)
        display_data_pretty(data)
    else:
        print("❌ Invalid choice!")


# MAIN PROGRAM
if __name__ == "__main__":
    print("🚀 REST API DATA CONSUMER")
    print("=" * 50)

    demo_apis()