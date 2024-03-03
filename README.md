# Search_Resume_Using_LLM_GENAI

Search Your Resume PDF App using the following technologies:

Langchain: An open-source framework for constructing natural language processing (NLP) workflows. It allows you to design and connect different NLP tasks in a modular way.
ChromaDB: A vector database specifically designed for efficient storage and retrieval of textual data embeddings. In this context, it's likely used to store representations of the PDFs for faster searching.
Open Source Large Language Model (LLM): The video might showcase how to integrate an open-source LLM model for text understanding and information extraction from PDFs. This avoids relying on the OpenAI API, potentially making the app usable offline or on machines with limited internet access.
Here's a breakdown of the possible functionalities:

User Input: The app would likely accept a natural language search query from the user.
Langchain Workflow: Langchain might be used to structure the search process. It could involve:
Preprocessing the user's query (e.g., tokenization, stemming).
Utilizing the open-source LLM to understand the intent of the query.
Interacting with ChromaDB to search for relevant keywords or concepts within the stored PDF embeddings.
Retrieving and Presenting Results: Based on the search results in ChromaDB, the app might display relevant portions of the PDFs that match the user's query.
Additional Considerations:

The video might delve into the technical details of setting up and using Langchain, ChromaDB, and the chosen LLM model.
It could also cover aspects of data preparation, such as converting PDFs to text and generating embeddings for ChromaDB.
There might be a discussion on the limitations and potential improvements of using an open-source LLM compared to a commercial solution like OpenAI.
Overall, the video is likely a tutorial on building a user-friendly search application for PDF documents using open-source tools and avoiding reliance on external APIs.

Project name: A clear and concise title for your project.
Description: A brief overview of what your project does and its key features.
Installation: Instructions on how to install and set up your project.
Usage: How to use your project, including any command-line arguments or configuration options.
Contributing: Guidelines for how others can contribute to your project.
License: The license under which your project is distributed.
You can also include additional sections in your README, such as:

Screenshots or demos: Visual examples of how your project works.
API documentation: If your project has an API, documentation on how to use it.
Changelog: A history of changes made to your project.
