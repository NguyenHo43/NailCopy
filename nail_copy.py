import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

MOCK_MODE = False  # set to True to test for free, without calling the real API

def generate_description_mock(service_desc: str) -> str:
    return f"This {service_desc} set is bold, elegant, and right on trend!"

def generate_description_real(service_desc: str) -> str:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("Missing ANTHROPIC_API_KEY in environment (.env)")

    client = Anthropic(api_key=api_key)

    prompt = (
        f"Write one short, catchy marketing sentence (under 30 words) "
        f"for this nail service: {service_desc}. "
        f"Return only the sentence, no explanation."
    )

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=100,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text.strip()

def main():
    print("=== NailCopy - Nail Marketing Description Generator ===\n")
    service_desc = input("Enter nail service description: ").strip()

    if not service_desc:
        print("You didn't enter anything.")
        return

    if MOCK_MODE:
        result = generate_description_mock(service_desc)
    else:
        result = generate_description_real(service_desc)

    print("\n--- Marketing description ---")
    print(result)

if __name__ == "__main__":
    main()