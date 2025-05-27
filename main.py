import os

def main():
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("No API key provided!")
        return

    # Simulate calling an external API
    print(f"Calling external API with key demo practical: {api_key[:4]}*** (hidden)")

if __name__ == "__main__":
    main()
