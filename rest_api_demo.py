import requests
import json
from datetime import datetime

print("🌐 REST API DEMO - Public APIs")
print("=" * 50)


def consume_public_apis():
    """Fetch and display data from public REST APIs"""

    apis = [
        {"name": "Users", "url": "https://jsonplaceholder.typicode.com/users"},
        {"name": "Random Quote", "url": "https://api.quotable.io/random"},
        {"name": "Random Joke", "url": "https://official-joke-api.appspot.com/random_joke"},
        {"name": "Cat Fact", "url": "https://catfact.ninja/fact"},
        {"name": "Dog Image", "url": "https://dog.ceo/api/breeds/image/random"}
    ]

    for i, api in enumerate(apis, 1):
        print(f"\n{i}️⃣  {api['name']} API")
        print("-" * 40)

        try:
            response = requests.get(api['url'], timeout=8)
            response.raise_for_status()
            data = response.json()

            print("✅ Success!")

            # Display data based on API
            if api['name'] == "Users":
                user = data[0] if isinstance(data, list) else data
                print(f"👤 {user.get('name', 'N/A')} - {user.get('email', 'N/A')}")
            elif api['name'] == "Random Quote":
                print(f"💬 '{data.get('content', 'N/A')}'")
                print(f"   — {data.get('author', 'Unknown')}")
            elif api['name'] == "Random Joke":
                print(f"😂 {data.get('setup', 'N/A')}")
                print(f"   {data.get('punchline', 'N/A')}")
            elif api['name'] == "Cat Fact":
                print(f"🐱 {data.get('fact', 'N/A')}")
            elif api['name'] == "Dog Image":
                print(f"🐶 {data.get('message', 'N/A')[:60]}...")

        except Exception as e:
            print(f"❌ Error: {str(e)[:50]}...")

    print("\n🎉 All public APIs consumed successfully!")


# Single API showcase with full JSON
def showcase_single_api():
    print("\n🔍 FULL JSON EXAMPLE - GitHub User")
    print("-" * 40)
    try:
        response = requests.get("https://api.github.com/users/octocat", timeout=5)
        user_data = response.json()

        print(json.dumps({
            "name": user_data.get("name"),
            "login": user_data.get("login"),
            "followers": user_data.get("followers"),
            "repos": user_data.get("public_repos"),
            "created": user_data.get("created_at")
        }, indent=2))

    except Exception as e:
        print(f"❌ Error: {e}")


# MAIN EXECUTION
if __name__ == "__main__":
    print(f"🕒 Started: {datetime.now().strftime('%H:%M:%S')}")

    consume_public_apis()
    showcase_single_api()

    print("\n✅ Demo complete! All APIs are FREE & PUBLIC.")