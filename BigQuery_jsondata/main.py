import requests
import os
from google.cloud import bigquery
from google.oauth2 import service_account
newsapi_key = "e7b0f56cb1384b13a12e6b4c446e504e"

def apicall_commerzbank():
    url = "https://newsapi.org/v2/everything?q=Commerzbank&apiKey=" + newsapi_key
    response = requests.get(url)
    articles = response.json()["articles"]
    filtered_articles = [article for article in articles if article["source"]["id"] != None]

    #print(filtered_articles)
    return filtered_articles

def apicall_source():
    url = "https://newsapi.org/v2/sources?apiKey=" + newsapi_key
    response = requests.get(url)
    sources = response.json()["sources"]
    #print(sources)
    return sources

def loaddata():

    #bq_file_path = 'bigquery_service_account_file.json'
    # Get the path to the credentials file from the GOOGLE_APPLICATION_CREDENTIALS environment variable
    credentials_path = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
    bq_credentials = service_account.Credentials.from_service_account_file(credentials_path)
    project_id = 'isg-dwh-bigquery'
    client = bigquery.Client(credentials= bq_credentials,project=project_id)
    dataset_id = "test_news_data"

    # Create the dataset
    dataset = bigquery.Dataset(bigquery.DatasetReference(client.project, dataset_id))
    dataset.location = "EU"
    dataset = client.create_dataset(dataset,exists_ok=True) # not to create again

    # Create the 'articles' table
    table_id = "articles"
    table = bigquery.Table(dataset.table(table_id))
    #table.schema = [bigquery.SchemaField("title", "STRING"),    bigquery.SchemaField("description", "STRING"),    bigquery.SchemaField("url", "STRING"),    bigquery.SchemaField("publishedAt", "TIMESTAMP"),    bigquery.SchemaField("source_id", "STRING"),]
    # bigquery.SchemaField("source", "RECORD", mode="REPEATED" , still thinking about repeated
    #https://cloud.google.com/bigquery/docs/nested-repeated
    table.schema = [
                bigquery.SchemaField("source", "RECORD", mode="NULLABLE",
                fields=[
                        bigquery.SchemaField("id", "STRING", mode="NULLABLE"),
                        bigquery.SchemaField("name", "STRING", mode="NULLABLE")
                        ]),
                bigquery.SchemaField("author", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("title", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("description", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("url", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("urlToImage", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("publishedAt", "TIMESTAMP", mode="NULLABLE"),
                bigquery.SchemaField("content", "STRING", mode="NULLABLE")
            ]

    table = client.create_table(table,exists_ok=True)
    print(f"Table {table.table_id} created successfully.")

    # Load the articles data into the 'articles' table
    filtered_articles = apicall_commerzbank()
    rows_to_insert = [{
        "source": {"id": row["source"]["id"], "name": row["source"]["name"]},
        "author": row["author"],
        "title": row["title"],
        "description": row["description"],
        "url": row["url"],
        "urlToImage": row["urlToImage"],
        "publishedAt": row["publishedAt"],
        "content": row["content"],
        }for row in filtered_articles]

    errors = client.insert_rows(table, rows_to_insert)  # Insert the rows into the table

    if not errors:
        print(f"{len(rows_to_insert)} rows successfully inserted into {table.table_id}.")
    else:
        print(f"Encountered errors while inserting rows: {errors}")

    # Create the 'sources' table
    table_id = "sources"
    table = bigquery.Table(dataset.table(table_id))
    table.schema = [ bigquery.SchemaField("id", "STRING"),    bigquery.SchemaField("name", "STRING"),    bigquery.SchemaField("description", "STRING"),    bigquery.SchemaField("url", "STRING"),    bigquery.SchemaField("category", "STRING"),    bigquery.SchemaField("language", "STRING"),    bigquery.SchemaField("country", "STRING"),]
    table = client.create_table(table,exists_ok=True)
    print(f"Table {table.table_id} created successfully.")

    # Load the sources data into the 'sources' table
    sources = apicall_source()

    rows_to_insert = [(source["id"], source["name"], source["description"], source["url"], source["category"], source["language"], source["country"]) for source in sources ]
    errors = client.insert_rows(table, rows_to_insert)
    # Check for errors
    if errors == []:
        print(f"{len(rows_to_insert)} rows successfully inserted into {table.table_id}.")
    else:
        print("Errors occurred while inserting data:")
        for error in errors:
            print(error)

    #setup the sqlquery
    query = """SELECT a.source.id, a.title, a.description, a.url, a.publishedAt, s.name
    FROM `test_news_data.articles` a
    JOIN `test_news_data.sources` s
    ON a.source.id = s.id
    limit 10; """
    # Run the query
    query_job = client.query(query)

    # Print the results
    print("the results of the query is: ")
    for row in query_job:
        print(row)


if __name__ == '__main__':
    loaddata()

