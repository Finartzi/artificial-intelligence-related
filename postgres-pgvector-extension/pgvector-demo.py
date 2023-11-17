from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

loader = TextLoader('./resources/state_of_the_union.txt', encoding='utf-8')
documents = loader.load()
print(documents)
print(len(documents))