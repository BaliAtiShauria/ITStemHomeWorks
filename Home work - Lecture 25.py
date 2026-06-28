import requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from requests.exceptions import Timeout, RequestException


BASE_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_posts(user_id):
    try:
        response = requests.get(
            BASE_URL,
            params={"userId": user_id},
            timeout=5
        )

        response.raise_for_status()

        print(f"User {user_id} პოსტები ჩამოიტვირთა.")
        return response.json()

    except Timeout:
        print(f"User {user_id} გამოტოვებულია: მოთხოვნას 5 წამზე მეტი დასჭირდა.")
        return []

    except RequestException as e:
        print(f"User {user_id} მოთხოვნის შეცდომა:", e)
        return []


def count_posts(all_posts):
    result = {}

    for post in all_posts:
        user_id = post["userId"]

        if user_id not in result:
            result[user_id] = 0

        result[user_id] += 1

    return result


def find_longest_post(all_posts):
    if not all_posts:
        return None

    longest_post = max(all_posts, key=lambda post: len(post["body"]))

    return {
        "userId": longest_post["userId"],
        "title": longest_post["title"],
        "length": len(longest_post["body"])
    }


def average_title_length(all_posts):
    if not all_posts:
        return 0

    total_length = 0

    for post in all_posts:
        total_length += len(post["title"])

    return total_length / len(all_posts)


def print_results(post_counts, longest_post, average_length):
    print("\n========================================")
    print("        პოსტების ანალიზი")
    print("========================================")

    print("მომხმარებელი   პოსტების რაოდენობა")
    print("------------------------------------")

    for user_id in sorted(post_counts):
        print(f"User {user_id:<14}{post_counts[user_id]}")

    print("\nყველაზე გრძელი პოსტი:")

    if longest_post:
        print(f"  მომხმარებელი: User {longest_post['userId']}")
        print(f"  სათაური: \"{longest_post['title']}\"")
        print(f"  სიგრძე: {longest_post['length']} სიმბოლო")
    else:
        print("  პოსტი ვერ მოიძებნა.")

    print(f"\nსათაურების საშუალო სიგრძე: {average_length:.2f} სიმბოლო")
    print("========================================")


def main():
    user_ids = [1, 2, 3, 4, 5]

    all_posts = []

    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(fetch_posts, user_ids))

    for user_posts in results:
        all_posts.extend(user_posts)

    with ProcessPoolExecutor() as executor:
        f1 = executor.submit(count_posts, all_posts)
        f2 = executor.submit(find_longest_post, all_posts)
        f3 = executor.submit(average_title_length, all_posts)

        post_counts = f1.result()
        longest_post = f2.result()
        average_length = f3.result()

    print_results(post_counts, longest_post, average_length)


if __name__ == "__main__":
    main()