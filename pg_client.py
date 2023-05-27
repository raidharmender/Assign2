import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="admin",
    password="secret",
    database="your_database_name"
)

# Create a cursor to execute SQL queries
cur = conn.cursor()

# Create a table
cur.execute("CREATE TABLE IF NOT EXISTS sample_data (id serial PRIMARY KEY, name varchar);")

# Insert sample data
cur.execute("INSERT INTO sample_data (name) VALUES ('John');")
cur.execute("INSERT INTO sample_data (name) VALUES ('Jane');")

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
