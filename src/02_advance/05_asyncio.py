import asyncio

import httpx

urls = [
    # "https://typicode.com",  # Mock blog post data
    # "https://typicode.com",  # Array of mock comments
    # "https://zippopotam.us",  # Location data for Beverly Hills ZIP code
    # "https://appspot.com",  # Random joke setup and punchline
    # "https://coindesk.com",  # Real-time Bitcoin prices
    "https://dog.ceo",  # Random dog image URL structure
    "https://catfact.ninja",  # Random trivia fact about cats
    "https://publicapis.org",  # Directory of public APIs (large JSON)
    # "https://httpbin.org",  # Standard mock JSON response page
    # "https://httpbin.org",  # Echoes back the JSON headers you sent
]


async def fetch(client: httpx.AsyncClient, url: str) -> httpx.Response:
    response = await client.get(url)
    data = response.json()
    return data


async def main():
    async with httpx.AsyncClient() as client:
        result = await asyncio.gather(
            *(fetch(client, url) for url in urls), return_exceptions=True
        )

    pretty_response = [{"body": res} for res in result]
    print(pretty_response)


if __name__ == "__main__":
    asyncio.run(main())
