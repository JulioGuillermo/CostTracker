# CostTracker

## Init venv

```bash
# creating venv
python -m venv my_venv

# activating venv
source my_venv/bin/activate
```

## Instaling dependencies

```bash
pip install django
pip install djangorestframework
```

## Run project

```bash
# go to the project folder
cd /path/to/the/CostTracker

# generate migrations and apply them
python manage.py makemigrations
python manage.py migrate

# create a superuser
python manage.py createsuperuser

# run the project
python manage.py runserver
```

Now the project is running, you can open this url in your web browser:

[localhost:8000/cost/list](http://localhost:8000/cost/list)

## API

### List all cost

To list the costs use this endpoint `GET /cost/api/costs/`

```bash
curl -u youruser:yourpass -H "Accept: application/json" -X GET http://127.0.0.1:8000/cost/api/costs/
```

You can filter the list of cost by:

- category
- amount
- date

To apply a filter add to the endpoint's url the filter.

For example to get all the cost with amount equals to 2:

```bash
curl -u youruser:yourpass -H "Accept: application/json" -X GET http://127.0.0.1:8000/cost/api/costs/?amount=2
```

### Get cost details

To get a cost's details use this endpoint `GET /cost/api/costs/<id>/`

```bash
curl -u youruser:yourpass -H "Accept: application/json" -X GET http://127.0.0.1:8000/cost/api/costs/<id>/
```

### Create new cost

To create a new cost use this endpoint `POST /cost/api/costs/`

```bash
curl -u youruser:yourpass -X POST http://127.0.0.1:8000/cost/api/costs/ -F "file=@/path/to/file" -F 'date="2023-02-08"' -F 'amount="1"' -F 'category="c1"'
```

### Edit a cost

To edit a cost use this endpoint `PUT /cost/api/costs/<id>/`

```bash
curl -u youruser:yourpass -X PUT http://127.0.0.1:8000/cost/api/costs/<id>/ -F "file=@/path/to/file" -F 'date="2023-02-18"' -F 'amount="1"' -F 'category="c2"'
```

### Remove a cost

To remove a cost use this endpoint `DELETE /cost/api/costs/<id>/`

```bash
curl -u youruser:yourpass -X DELETE http://127.0.0.1:8000/cost/api/costs/<id>/
```
