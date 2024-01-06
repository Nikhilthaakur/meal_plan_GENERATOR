import streamlit as st
import requests
import random

# Function to generate a meal plan based on user inputs
def generate_meal_plan(no_of_meals, diet_preference, health_specification, calories, spoonacular_api_key):
    # Use the Spoonacular API to retrieve recipe information
    spoonacular_api_url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "query": diet_preference,
        "number": no_of_meals * 5,  # Fetch more recipes to ensure enough unique ones
        "diet": health_specification,
        "apiKey": spoonacular_api_key,
    }

    response = requests.get(spoonacular_api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        recipes = data.get("results", [])

        if recipes:
            meal_plan = generate_dummy_meal_plan(recipes, no_of_meals)
            return meal_plan
        else:
            st.error("No recipes found for the given criteria.")
            return None
    else:
        st.error("Error fetching data from Spoonacular API")
        return None

# Function to generate a dummy meal plan with unique meals for each day
def generate_dummy_meal_plan(recipes, no_of_meals):
    # Shuffle the recipes randomly
    random.shuffle(recipes)

    # Replace this with your actual logic for generating a meal plan
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    meal_plan = {}

    for day in days_of_week:
        meals = []
        for i in range(1, no_of_meals + 1):
            if recipes:
                random_recipe = recipes.pop()
                meals.append({
                    "name": random_recipe.get("title", ""),
                    "id": random_recipe.get("id", ""),
                    "image": random_recipe.get("image", ""),
                    "ingredients": random_recipe.get("missedIngredients", []) + random_recipe.get("usedIngredients", []),
                })
            else:
                meals.append({
                    "name": f"Meal {i}",
                    "image": "",
                    "ingredients": ["Ingredient 1", "Ingredient 2", "Ingredient 3"],
                })

        meal_plan[day] = meals

    return meal_plan

# Function to display the meal plan
def display_meal_plan(meal_plan):
    st.write("## Meal Plan")

    weekdays = list(meal_plan.keys())

    for i in range(len(meal_plan[weekdays[0]])):
        st.write(f"### Meal {i + 1}")

        # Create columns for each day
        cols = st.columns(len(weekdays))

        for j, day in enumerate(weekdays):
            meal = meal_plan[day][i]

            # Display meal information in each column
            with cols[j]:
                st.subheader(day)
                st.write(f"**{meal['name']}**")
                st.image(meal['image'], use_column_width=True)
                st.write("Ingredients:", ", ".join(meal['ingredients']))

                # Add a button to show more information when clicked
                button_key = f"more_info_{day}_{i}"  # Unique key for each button
                if st.button("More Info", key=button_key):
                    show_meal_info(meal['id'])

# Function to show more information about a meal
def show_meal_info(meal_id):
    st.write("## Meal Information")

    # Use the Spoonacular API to get detailed information about the meal
    spoonacular_api_url = f"https://api.spoonacular.com/recipes/{meal_id}/information"
    params = {"apiKey": '777d125cc30a442f8d1a35f5b65be131'}  # Replace with your actual key

    response = requests.get(spoonacular_api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        st.subheader(data.get("title", ""))
        st.image(data.get("image", ""), use_column_width=True)
        st.write("Ingredients:", ", ".join([ingredient.get("name", "") for ingredient in data.get("extendedIngredients", [])]))
        st.write("Instructions:", data.get("instructions", "No instructions available."))
    else:
        st.error("Error fetching meal information from Spoonacular API")

def main():
    st.title("Meal Plan Generator")

    # Form to get user inputs
    no_of_meals = st.selectbox("Number of Meals:", [2, 3, 5])
    diet_preference = st.selectbox("Diet Preference:", ["Balanced", "Low Carb", "Low Fat"])
    health_specification = st.selectbox("Health Specification:", ["Vegan", "Vegetarian", "Alcohol Free", "Peanut Free"])
    calories = st.number_input("Calories:", min_value=0, step=1)

    # Spoonacular API key (replace with your actual key)
    spoonacular_api_key = '777d125cc30a442f8d1a35f5b65be131'

    # Button to generate meal plan
    if st.button("Generate Meal Plan"):
        meal_plan = generate_meal_plan(no_of_meals, diet_preference, health_specification, calories, spoonacular_api_key)

        if meal_plan:
            display_meal_plan(meal_plan)

if __name__ == "__main__":
    main()
