## API Key Creation

To access customer data via API the first step is to create an API Key.

Go to Admin > Generate API Key and press the Generate button.

![Generate API Key](../assets/images/customer-data/api/api-key-generate.png)

Copy the generated API Key as it will only be displayed once.

You can use the same page to delete an existing key and create a new one if needed.

This API key will need to set as the value of the `X-API-Key` header when making API requests.

The URL for API requests will be:

```
https://<hostname>/api
```

This will be followed by the specific endpoint that you're querying.

## Customers

Customer data can be retrieved using the customers API. If using multi-tenancy replace `default` with the team identifier.

```
Request Type: GET
API Endpoint: /customers
Query Parameters: slug=default
```

![Get Customers](../assets/images/customer-data/api/api-customers.png)

## Customer Visits

Customer visit data can be retrieved using the customer-visits API. If using multi-tenancy replace `default` with the team identifier.

```
Request Type: GET
API Endpoint: /customer-visits
Query Parameters: slug=default
```

![Get Customer Visits](../assets/images/customer-data/api/api-visits.png)