import asyncio
import aiohttp

class PostAnalyzer:

    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com/posts"
        self.user_ids = [1, 2, 3, 4, 5]
        self.all_posts = []

    async def fetch_posts(self, session, user_id):
        try:
            async with session.get(
                    self.base_url,
                    params={"userId": user_id}
            ) as response:

                response.raise_for_status()

                posts = await response.json()

                print(f"User {user_id} downloaded.")

                return posts

        except asyncio.TimeoutError:
            print(f"User {user_id} timeout.")
            return []

        except aiohttp.ClientError as e:
            print(e)
            return []

    async def download_posts(self):

        timeout = aiohttp.ClientTimeout(total=5)

        async with aiohttp.ClientSession(timeout=timeout) as session:

            tasks = []

            for user_id in self.user_ids:
                tasks.append(
                    self.fetch_posts(session, user_id)
                )

            results = await asyncio.gather(*tasks)

            for posts in results:
                self.all_posts.extend(posts)

    def count_posts(self):

        result = {}

        for post in self.all_posts:

            user = post["userId"]

            if user not in result:
                result[user] = 0

            result[user] += 1

        return result

    def find_longest_post(self):

        if not self.all_posts:
            return None

        longest = max(
            self.all_posts,
            key=lambda post: len(post["body"])
        )

        return longest

    def average_title_length(self):

        if not self.all_posts:
            return 0

        total = 0

        for post in self.all_posts:
            total += len(post["title"])

        return total / len(self.all_posts)

    def print_results(self):

        counts = self.count_posts()

        longest = self.find_longest_post()

        average = self.average_title_length()

        print("\n===================================")
        print("      პოსტების ანალიზი")
        print("===================================")

        print("\nმომხმარებელი | პოსტები")

        for user in sorted(counts):
            print(f"User {user} -> {counts[user]}")

        print("\nყველაზე გრძელი პოსტი")

        print(f"User: {longest['userId']}")
        print(f"Title: {longest['title']}")
        print(f"Length: {len(longest['body'])}")

        print(f"\nსათაურების საშუალო სიგრძე: {average:.2f}")

    async def run(self):

        await self.download_posts()

        self.print_results()


if __name__ == "__main__":

    analyzer = PostAnalyzer()

    asyncio.run(analyzer.run())