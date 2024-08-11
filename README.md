This repository contains code for two RAG applications with access to information from FrameNet version 1.7. ChatGPT-3.5-turbo (stage 2) and Mixtral 8x22B (stage 3) are used as LLMs, and AstraDB is used as a vector store. Information for each frame is stored as an individual embedding and includes the definition, core FEs and their definitions, lexical units, and frame relations. The model is designed to answer prompts concerning lexical unit generation such as: "Please propose 10 additional words that evoke the “XXXX” semantic frame." Steps for implentation and use are as follows:

1. Install Langflow (preferably in a virtual environment) using the command: python -m pip install langflow --pre --force-reinstall
2. Open the JSON file for the model you would like to use in Langflow.
3. Enter your own secret keys for OpenAI/Mistral where Langflow indicates.
4. Either run the model in Langflow or download the flow as a new JSON to run on your IDE.
5. When prompted by the program, input your question into the terminal.
