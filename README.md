
# Swagger Beispiel Endpunkte

Ein kleines Beispiel für ein Schulprojekt, wie man in Python eine Swagger Schnittstelle für eine API anbindet.

## Run Locally


1. Install packages 

```bash
  pip install flask, Flask-RESTful, flasgger
```

2. Run App
```bash
  python app.py
```

3. Visit http://localhost:5000/apidocs

## API Reference

#### Get all items

```http
  GET /items
```

#### Add item

```http
  GET /items/add/{item_name}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `item_name`| `string` | **Required**. Item to Add |


#### Remove item

```http
  GET /items/remove/{item_name}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `item_name`| `string` | **Required**. Item to Remove |

#### Update item

```http
  GET ​/items​/update
```

| Body | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `{new_value: "", old_value: ""}`| `JSON` | **Required**. Old Value to Uptade with new Value |

