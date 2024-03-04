# Search_Resume_Using_LLM_GENAI

Search Your Resume PDF App using the following technologies:

- Langchain: An open-source framework for constructing natural language processing (NLP) workflows. It allows you to design and connect different NLP tasks in a modular way.
- ChromaDB: A vector database specifically designed for efficient storage and retrieval of textual data embeddings. In this context, it's likely used to store representations of the PDFs for faster searching.
Open Source Large Language Model (LLM): The video might showcase how to integrate an open-source LLM model for text understanding and information extraction from PDFs. This avoids relying on the OpenAI API, potentially making the app usable offline or on machines with limited internet access.


Here's a breakdown of the possible functionalities:

- User Input: The app would likely accept a natural language search query from the user.
- Langchain Workflow: Langchain might be used to structure the search process. It could involve:
Preprocessing the user's query (e.g., tokenization, stemming).
Utilizing the open-source LLM to understand the intent of the query.
Interacting with ChromaDB to search for relevant keywords or concepts within the stored PDF embeddings.
- Retrieving and Presenting Results: Based on the search results in ChromaDB, the app might display relevant portions of the PDFs that match the user's query.


Additional Considerations:

The above code  delve into the technical details of setting up and using Langchain, ChromaDB, and the chosen LLM model.
It cover aspects of data preparation, such as converting PDFs to text and generating embeddings for ChromaDB.

