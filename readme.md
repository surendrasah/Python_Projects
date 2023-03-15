These folders will contain their respective programs

# Addressline
This Projects takes string of address as input and output the string of street and string of street-number as JSON object
It has been done using split method and regular expression.

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
        
# dataingestion_flaskapi_etl-main
An ingestion system for two data streams. It must accept HTTP messages. Example files are provided for both streams. The first stream named 'metrics.json' is an example of machine data. The second, 'workorder.json', defines what product ran when and how much output was produced. Persist this data. (time relates the two data sources). An ETL pipeline that reads the data from step 1, and finds the top three parameters that correlate to the production output of each product, and output them in a static report.

python3 data_app_ingestion.py : web api flask server proram
python3 data_post_request.py : load the data to database using post request
python3 data_store_etl.py : Etl program to read the data and correlation between product and production output

# deploy_lambda_with_terraform-main
Use terraform main.tf to execute lambda function

# docker-compose_with_mysql_python
This is a simple example to use docker-compose with mysql and python. Create a Docker image for loading the CSV files, places.csv and people.csv, into the tables
you have created in the database. Make sure the appropriate config is in the docker compose file. Your data ingest process can be implemented in any way that you like, as longas it runs within a Docker container. You may implement this via programme code in a Python, or via the use of ETL tools.  You may implement this using Python. The output must be in JSON format, and be written to a file in the data folder called **data/summary_output.json**. It should consist of a list of the countries, and a count of how many people were born in that country. We have supplied a sample output **data/sample_output.json** to compare your file against.


# docker_compose_mysql_environmentdata
The data relates to environmental profiles and layers, with information about the location, depth range, and organic matter content of the layers.
This program contains config.yml, csv file and 

volumes:
      
      - ./data/table_schema.sql:/docker-entrypoint-initdb.d/schema.sql
    
