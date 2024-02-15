# LAB - Class 28

## Project: Snacks Crud

- Author: Ekow Yawson

### Overview

In this iteration, we will add a full **CRUD** functionality to our bag of tricks by building a Django project that allows `Creating`, `Reading`, `Updating` and `Deleting`.

### Links and Resources

- [What is Django](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction)
- [First Django App - Part 1](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)
- [First Django App - Part 2](https://docs.djangoproject.com/en/4.1/intro/tutorial02/)
- [Django Forms](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms)
- [Django Templates](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page)
- [Django Views](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views)
- [What is Tailwind CSS?](https://blog.hubspot.com/website/what-is-tailwind-css)
- [Tailwind CSS Django - Flowbite](https://flowbite.com/docs/getting-started/django/)

### Feature Tasks and Requirements

- [x] Create snacks app
- [ ] Create Snack model
  - `title` field
  - `purchaser` field
  - `description` field
  - Register model with `admin`
- [ ] Create SnackListView that extends appropriate generic view
  - Associated url path is an empty string
- [ ] Create SnackDetailView that extends appropriate generic view
  - Associated url path is <int:pk>/
- [ ] Create SnackCreateView that extends appropriate generic view
  - Associated url path is create/
- [ ] Create SnackUpdateView that extends appropriate generic view
  - Associated url path is <int:pk>/update/
- [ ] Create SnackDeleteView that extends appropriate generic view
  - Associated url path is <int:pk>/delete/
- [ ] Add urls to support all views, with appropriate names
- [ ] Add templates to support all views
- [ ] Add navigation links in appropriate locations to access all pages
- [ ] Make all necessary changes to project level files for project to run

### Stretch Goals

- [ ] Add multiple models
- [ ] Use an alternate test runner
- [ ] Add more advanced fields to models, e.g. created time stamp
- [ ] Add styling

### Setup

#### How to initialize/run your application

To run this app, you must:

1. Create a Python virtual environment.
2. Enter the virtual environment.
3. Run `pip install -r requirements.txt`
4. Run the server with: `python manage.py runserver`
5. Follow the link provided in the CLI.

**Note**: This is a development build. Do not run it in Production.

### Tests

- [ ] Test all Views
- [ ] Test Model
  - String representation
  - All fields

To run the contained tests, issue the following command in the CLI:

```bash
python manage.py test
```
