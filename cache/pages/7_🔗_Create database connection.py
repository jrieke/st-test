client = st.connect("bigquery", ttl=24*3600, **kwargs)
client.query("SELECT * FROM table")

client = st.connect_bigquery()
client.query("SELECT * FROM table") # <-- This is auto-memoized! 

