from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

loader = TextLoader('./resources/state_of_the_union.txt', encoding='utf-8')
documents = loader.load()
#print(documents)
print(len(documents))

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=80)
texts = text_splitter.split_documents(documents)
#print(texts[0])
print(len(texts))