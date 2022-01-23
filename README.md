# Stock Trader

![Lint workflow](https://github.com/MarvinKweyu/stock-trader/actions/workflows/lint.yml/badge.svg?branch=main)
[![Python](https://img.shields.io/badge/python-%7C3.7%7C3.8%7C3.9-green)](https://github.com/MarvinKweyu/stock-trader)

> An API for an inventory management and re-order application

## Local setup

Clone the application, install requirements and run the local server

```bash
pip install -r requirements.txt
python manage.py runserver
```

To access the api:

`127.0.0.1:8000/api/v1/`

For documentation:

`127.0.0.1:8000/api/v1/docs`



## Current users:

**Retailer**

```
username: retailer
email: retailer@mail.com
password: retailer
```

**Warehouse attendant**

```
username: attendant2
email: attendant2@mail.com
password: attendant2
```

To make a product sale, make a `patch` request to the product endpoint , changing the product amount as needed.

<br/>

To make a dispatch from the warehouse, make a similar update request to tehe `reorder` endpoint **changing the status of the reorder.**


# Contribution

To contribute to this project, please fork the repository and make a pull request.

```bash
pre-commit install
```

Run against all files
```bash
pre-commit run --all-files
```
## Tests

```bash
pytest
```

## More Documentation

For development using django and articles around software engineering, please visit [TheGreenCodes](https://thegreencodes.com/).

