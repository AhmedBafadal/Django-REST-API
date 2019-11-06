# Django REST API
## Description
This project is a production ready REST API, implemented using test driven development (TDD). The API developed was designed to organise users' favourite recipes, and is capable of handling authentication, creation of objects, filtering objects, and uploading of images.

The API was built using Python, Django, Django Rest Framework and Pillow. Further, this project leverages Docker, Postgresql and Travis CI in the interest of development best practices.

This API enables users to create a new account, generate new authentication tokens upon logging in, create ingredients for recipes as well as tags that reference recipes (e.g. "Vegan"). Through the API, users can filter recipes based on the ID of either ingredients & tags, and it is possible to filter using both ingredients & tags simultaneously (e.g. 127.0.0.1:8000/api/recipes/recipes/?tags=2&ingredients=1). Further, it is also possible to filter tags & ingredients based on if they are assigned to any recipe (e.g. 127.0.0.1:8000/api/recipe/tags/?assigned_only=1).

## Installation
```
docker-compose up --build

```

## Implementation
Upon running the app, users can add recipe titles, ingredients, cooking time, tags (for searching and filtering recipes in the system) & images. Workflow is as below:

!Note: Please use Google Chrome extension Mod Header or alternative to add authentication token to header in browser.

List of api urls found at localhost:8000/api/recipe

1. Create a new user at endpoint /api/user/create.

2. Access & Login at endpoint /api/user/token to generate authentication token.

3. Access endpoint /api/recipe/ingredients to create a new ingredient.

4. Access endpoint /api/recipe/tags to create tags which represent the recipe.

5. Access endpoint /api/recipe/recipes to create full recipe.

6. To add images to recipes, from the /api/recipe/recipes endpoint append the ID of the recipe into the url to edit recipe (e.g. 127.0.0.1/api/recipe/recipes/2). 
Further, to add an image, append upload-image to url (e.g. 127.0.0.1/api/recipe/recipes/2/upload-image).

7. Once tags & ingredients added. In api/recipes/tags endpoint, it is possible to filter either ingredients or tags to only the tags which are assigned to a recipe. (e.g. 127.0.0.1:8000/api/recipe/tags/?assigned_only=1), and assigned_only=0 returns all tags unassigned to recipe.

8. In /api/recipe/recipes endpoint, it is possible to filter by ingredient ID (e.g. 127.0.0.1:8000/api/recipes/recipes/?ingredients=2). This feature is also replicated for tags. NOTE: it is also possible to filter by both tags and ingredients (e.g. 127.0.0.1:8000/api/recipes/recipes/?tags=2&ingredients=1).

