# PetStore API
`https://petstore.swagger.io/v2`

## Contents
1. [Introduction](#introduction-petstore-company)
2. [How to use the PetStore API](#how-to-use-the-petstore-api)
   1. [Register a pet](#register-a-pet)
   2. [Get details of a pet](#get-details-of-a-pet)
   3. [Remove a pet](#remove-a-pet)
   4. [Error message format](#error-message-format)
3. [Integration with PetStore API](#integration-with-petstore-api)

## Introduction: PetStore Company
Operating a pet store is a fast-paced endeavor that can become difficult to organize as pets come and go. The PetStore 
company aims to reduce the complexity of pet store operations by providing a number of digital tools designed with the 
pet store operator in mind.

PetStore builds and maintains an open-source toolkit that provides essential functionality for pet stores around the 
world. One of these functions is a database to keep track of new pets that are added to the store and when they are 
adopted. Details of these pets are stored alongside their availability status in a database. PetStore has an API for 
easy use and integration.

## How to use the PetStore API
The PetStore API has standard REST endpoints. The base URL is `https://petstore.swagger.io/v2`

### Register a pet
The endpoint to register a pet and its details is POST `/pet`.

An example is below. The variables and their types needed are:
- id: integer
- category: dict `{id: integer, name: string}`
- name: string
- photoUrls: list of strings
- tags: OrderedMap `[{id: integer, name: string}]`
- status: enum `[available, pending, sold]`

```
{
  "id": 6,
  "category": {
    "id": 1,
    "name": "dog"
  },
  "name": "snoopy",
  "photoUrls": [
    "https://pngimg.com/uploads/snoopy/snoopy_PNG23.png"
  ],
  "tags": [
    {
      "id": 1,
      "name": "allergenic"
    }
  ],
  "status": "available"
}
```

### Get details of a pet
To find information about a  pet, use GET `/pet/{petId}`. If successful, the response is the same format as the 
[register a pet](#register-a-pet) JSON above.

### Remove a pet
To remove a pet from the database use DELETE `/pet/{petId}`.

### Error message format
If the API cannot complete a request, an error message containing `code`, `type`, and `message` will be sent back.
```
{
  "code": 404,
  "type": "unknown",
  "message": "java.lang.NumberFormatException: string format"
}
```

## Integration with PetStore API
### Code example
An example of integration with the PetStore API using Python is below. Here, 10 pets with unique names are selected 
that have `status=available` in the database. This example uses the GET `/pet/findByStatus` endpoint.

```python
import requests

# Set endpoint with status=available
endpoint = 'https://petstore.swagger.io/v2/pet/findByStatus?status=available'

# Use GET request, convert to json
data = requests.get(url=endpoint).json()

# Set up starting variables
i = 0
counter = 0
names = []

# Select 10 pets with unique names
while counter < 10:

    # If name is unique
    if data[i]['name'] not in names:

        # Add name to non-unique list
        names.append(data[i]['name'])

        # Print out id and name, add 1 to count
        print(data[i]['id'], data[i]['name'])
        counter += 1

    # Move to next pet in data
    i += 1
```

### Output
```
9223372036854545336 doggie
9223372036854545338 toddy
9223372036854545362 fish
99996 doggie_by_ms
9223372036854545422 Doggie
1950 pammy
9223372036854545479 siyaan
888 Chiola
50 iRLZZCzi3c
91 aWXVcaXs7C
```


