# Healthy Recipe & Meal Planner

## Overview
The Healthy Recipe & Meal Planner is a web application designed to help users plan their meals and discover healthy recipes. It aims to promote healthy eating habits by providing a user-friendly interface for meal planning and recipe exploration.

## Features
- **Recipe Search**: Find healthy recipes based on ingredients, dietary preferences, and meal types.
- **Meal Planning**: Create and manage weekly meal plans with ease.
- **Shopping List**: Automatically generate shopping lists based on selected recipes.
- **User Accounts**: Save favorite recipes and meal plans by creating an account.
- **Nutritional Information**: View detailed nutritional information for each recipe.

## Technologies Used
- **Framework**: Django
- **Database**: SQLite3
- **Dependency Management**: Poetry

## Installation
To get started with the Healthy Recipe & Meal Planner, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/muratbekj/Team8_HW.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Team8_HW
   ```
3. Install Poetry

4. Install the dependencies:
   ```bash
   poetry install
   ```
5. Run database migrations:
   ```bash
   poetry run python manage.py migrate
   ```
6. Start the application:
   ```bash
   poetry run python manage.py runserver
   ```

## Usage
Once the application is running, you can:
- Search for recipes using the search bar.
- Add recipes to your meal plan by clicking on the "Add to Meal Plan" button.
- View your meal plan and shopping list in the respective sections.

