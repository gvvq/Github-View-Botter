import asyncio
import aiohttp
import time

async def make_request(session, url, semaphore):
    async with semaphore:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    print("Request successful")
        except aiohttp.ClientError as e:
            pass

async def main():
    url = "https://visitor-badge.laobi.icu/badge?page_id=gvvq.gvvq"
    num_requests = 1000000
    concurrency_limit = 1000
    start_time = time.time()
    semaphore = asyncio.Semaphore(concurrency_limit)
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=None)) as session:
        tasks = [make_request(session, url, semaphore) for _ in range(num_requests)]
        await asyncio.gather(*tasks)
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Took {total_time} seconds")

if __name__ == "__main__":
    asyncio.run(main())
