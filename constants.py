import os 
from chromadb.config import Settings 

# #Define the chroma settings
# CHROMA_SETTINGS = Settings(
#     chroma_db_impl = 'duckdb+parquet',
#     persist_directory = "database",
#     anonymized_telemetry = False
# )

# # # before
# # import chromadb
# # from chromadb.config import Settings
# # client = chromadb.Client(Settings(
# #     chroma_db_impl="duckdb+parquet",
# #     persist_directory="/path/to/persist/directory" # Optional, defaults to .chromadb/ in the current directory
# # ))

# # after
import chromadb
CHROMA_SETTINGS = chromadb.PersistentClient(path="database")