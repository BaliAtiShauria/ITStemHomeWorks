import json
import requests
from pydantic import BaseModel, ValidationError
from requests.exceptions import HTTPError, ConnectTimeout


BASE_URL = "https://crudcrud.com/api/944e5d418a524edb8fa07bd903c34812/recipes"


class Recipe(BaseModel):
    name: str
    cuisine: str
    time_minutes: str


def load_recipes_from_json():
    try:
        with open("recipes.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        return [Recipe(**item) for item in data]

    except FileNotFoundError:
        print("recipes.json ფაილი ვერ მოიძებნა.")
        return []

    except ValidationError as e:
        print("Pydantic ვალიდაციის შეცდომა:", e)
        return []

    except Exception as e:
        print("ფაილის წაკითხვის შეცდომა:", e)
        return []


def post_recipes():
    recipes = load_recipes_from_json()

    for recipe in recipes:
        try:
            response = requests.post(
                BASE_URL,
                json=recipe.model_dump(),
                timeout=5
            )

            response.raise_for_status()

            print("დაემატა:", response.json())

        except HTTPError as e:
            print("HTTP შეცდომა POST-ში:", e)

        except ConnectTimeout:
            print("სერვერმა დიდხანს არ უპასუხა POST მოთხოვნაზე.")

        except ValidationError as e:
            print("Pydantic შეცდომა:", e)

        except Exception as e:
            print("POST შეცდომა:", e)


def get_all_recipes():
    try:
        response = requests.get(BASE_URL, timeout=5)
        response.raise_for_status()

        recipes = response.json()

        print("\nყველა რეცეპტი:")

        for recipe in recipes:
            print(f"{recipe['name']} - {recipe['time_minutes']} წუთი")

        return recipes

    except HTTPError as e:
        print("HTTP შეცდომა GET-ში:", e)

    except ConnectTimeout:
        print("სერვერმა დიდხანს არ უპასუხა GET მოთხოვნაზე.")

    except Exception as e:
        print("GET შეცდომა:", e)

    return []


def get_recipe_by_id(recipe_id):
    try:
        response = requests.get(f"{BASE_URL}/{recipe_id}", timeout=5)
        response.raise_for_status()

        recipe = response.json()

        print("\nერთი რეცეპტი ID-ით:")
        print(recipe)

        return recipe

    except HTTPError as e:
        print("HTTP შეცდომა GET BY ID-ში:", e)

    except ConnectTimeout:
        print("სერვერმა დიდხანს არ უპასუხა GET BY ID მოთხოვნაზე.")

    except Exception as e:
        print("GET BY ID შეცდომა:", e)

    return None


def update_recipe(recipe_id):
    try:
        updated_recipe = Recipe(
            name="Adjarian Khachapuri",
            cuisine="Georgian",
            time_minutes="35"
        )

        response = requests.put(
            f"{BASE_URL}/{recipe_id}",
            json=updated_recipe.model_dump(),
            timeout=5
        )

        response.raise_for_status()

        print("\nრეცეპტი განახლდა PUT მეთოდით.")

    except HTTPError as e:
        print("HTTP შეცდომა PUT-ში:", e)

    except ConnectTimeout:
        print("სერვერმა დიდხანს არ უპასუხა PUT მოთხოვნაზე.")

    except ValidationError as e:
        print("Pydantic ვალიდაციის შეცდომა PUT-ში:", e)

    except Exception as e:
        print("PUT შეცდომა:", e)


def delete_recipe(recipe_id):
    try:
        response = requests.delete(f"{BASE_URL}/{recipe_id}", timeout=5)
        response.raise_for_status()

        print("\nბოლო რეცეპტი წაიშალა.")

    except HTTPError as e:
        print("HTTP შეცდომა DELETE-ში:", e)

    except ConnectTimeout:
        print("სერვერმა დიდხანს არ უპასუხა DELETE მოთხოვნაზე.")

    except Exception as e:
        print("DELETE შეცდომა:", e)


def main():
    post_recipes()

    recipes = get_all_recipes()

    if not recipes:
        print("რეცეპტები არ მოიძებნა.")
        return

    first_recipe_id = recipes[0]["_id"]
    get_recipe_by_id(first_recipe_id)

    update_recipe(first_recipe_id)

    recipes = get_all_recipes()

    if recipes:
        last_recipe_id = recipes[-1]["_id"]
        delete_recipe(last_recipe_id)

    get_all_recipes()


main()