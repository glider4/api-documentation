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
