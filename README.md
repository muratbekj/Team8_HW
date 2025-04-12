# Healthy Recipe & Meal Planner

🧾 Overview
Healthy Recipe & Meal Planner is a Django-based web application designed to help users plan nutritious meals and discover healthy recipes. It promotes balanced eating habits through a user-friendly interface for meal planning, recipe exploration, and shopping list generation.

🚀 Features
🔍 Recipe Search – Find recipes based on ingredients, dietary preferences, and meal types.

👤 User Accounts – Register and log in to save your favorite recipes and meal plans.

🧪 Nutritional Information – View detailed nutrition facts for every recipe.

❤️ Save Recipes – Bookmark recipes to revisit later on your personal dashboard.

🛠️ Technologies Used
Framework: Django

Database: SQLite3 (default for development)

Frontend: HTML, CSS

Dependency Management: Poetry

📦 Installation
To get started with the project locally:

Clone the repository

```bash
git clone https://github.com/muratbekj/Team8_HW.git
cd Team8_HW
```

Install Poetry
If you haven't already, install Poetry from https://python-poetry.org/docs/#installation.

Install dependencies

```bash
poetry install
```

Apply database migrations

```bash
poetry run python manage.py migrate
```

Create a superuser (optional, for admin access)

```bash
poetry run python manage.py createsuperuser
```

Run the development server

```bash
poetry run python manage.py runserver
```

💡 Usage
Once the server is running:

🔎 Use the search bar to discover healthy recipes.

➕ Click "Add to Meal Plan" to include a recipe in your weekly plan.

📋 View and manage your meal plan and shopping list.

❤️ Save recipes and view them on your dashboard.

---

## Terminal Commands

Here are some useful terminal commands for managing your Django application:

```bash
# Start the development server
poetry run python manage.py runserver

# Apply migrations
poetry run python manage.py migrate

# Create a superuser
poetry run python manage.py createsuperuser

# Open the Django shell
poetry run python manage.py shell

# Collect static files
poetry run python manage.py collectstatic
```
```