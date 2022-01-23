# Stock Trader

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

## Test

```bash
pytest
```
