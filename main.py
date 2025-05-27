import os

def main():
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("No API key provided!")
        return

    # Simulate calling an external API
    print(f"Printing first 5 character with external API with key: {api_key[:5]}*** (hidden)")

if __name__ == "__main__":
    main()
