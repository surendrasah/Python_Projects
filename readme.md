These folders will contain their respective programs

# BigQuery_jsondata
This project ingests the api json data and loads it to the bigquery. The json data is complex, so we need to define the schema properly.
bigquery schema:

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
