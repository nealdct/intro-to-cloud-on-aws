# 1. Create a DynamoDB table

1. Create a DynamoDB table
2. Set the table name to `myorders`
3. Set the primary key to `clientid`
4. Set the sort key to `created`

# 2. Load items into the table

1. Open AWS CloudShell
2. Upload the `batch-write.json` file
3. Run the following command to load the entries from the file

```bash
aws dynamodb batch-write-item --request-items file://batch-write.json
```

4. Use the "Explore items" view under "Tables" to view the items in the table

# 3. Use Scan APIs to find data

1. This example demonstrates how to scan the myorders table for items in a specific category, such as "Electronics"

```bash
aws dynamodb scan \
    --table-name myorders \
    --filter-expression "category = :cat" \
    --expression-attribute-values '{":cat":{"S":"Electronics"}}'
```

```--filter-expression "category = :cat"``` specifies the condition to filter items where the category attribute equals a value we define
```--expression-attribute-values '{":cat":{"S":"Electronics"}}'``` defines the value for :cat used in the filter expression, in this case, "Electronics"

2. This example shows how to scan the myorders table for items where the quantity (qty) is greater than 2

```bash
aws dynamodb scan \
    --table-name myorders \
    --filter-expression "qty > :q" \
    --expression-attribute-values '{":q":{"N":"2"}}'
```
```--filter-expression "qty > :q"``` specifies the condition to filter items where the qty attribute is greater than a value we define
```--expression-attribute-values '{":q":{"N":"2"}}'``` defines the value for :q used in the filter expression, in this case, a quantity of 2

# 4. Use Query APIs to find data

1. This example demonstrates how to query the myorders table for all orders made by a specific client, identified by clientid

```bash
aws dynamodb query \
    --table-name myorders \
    --key-condition-expression "clientid = :clientid" \
    --expression-attribute-values '{":clientid":{"S":"client01@example.com"}}'
```
```--key-condition-expression "clientid = :clientid"``` specifies the condition for the query to find items where the clientid matches the specified value
```--expression-attribute-values '{":clientid":{"S":"client01@example.com"}}'``` defines the value for :clientid used in the key condition expression

2. If you want to find orders from a specific client within a certain date range, you can use the sort key (created) along with the partition key (clientid) in your query

```bash
aws dynamodb query \
    --table-name myorders \
    --key-condition-expression "clientid = :clientid AND created BETWEEN :date1 AND :date2" \
    --expression-attribute-values '{":clientid":{"S":"client01@example.com"}, ":date1":{"S":"2023-01-01T00:00Z"}, ":date2":{"S":"2023-01-31T23:59Z"}}'
```

```--key-condition-expression "clientid = :clientid AND created BETWEEN :date1 AND :date2"``` specifies the condition for the query to find items where the clientid matches the specified value and the created date falls within the specified range
```--expression-attribute-values '{":clientid":{"S":"client01@example.com"}, ":date1":{"S":"2023-01-01T00:00Z"}, ":date2":{"S":"2023-01-31T23:59Z"}}'``` defines the values for :clientid, :date1, and :date2 used in the key condition expression