from langchain_openai import ChatOpenAI,OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.runnables import RunnableLambda,RunnableParallel,RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_chroma import Chroma
load_dotenv()

loader = PyPDFLoader("test.pdf")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
chunks = splitter.split_documents(documents)

embedddings = OpenAIEmbeddings(
    model = "text-embedding-3-small",
)

vector_store = Chroma.from_documents(
    embedding=embedddings,documents=chunks
)


llm = ChatOpenAI(model='gpt-4o-mini',temperature=0.7)
prompt = PromptTemplate(
    template="""
you are helpfull assistant ,
give answers based on only context
if you didnt find answer in context the print only not found
context:{context}
result:{question} 
""",
input_variables=['context','question']
)

retriever = vector_store.as_retriever(
    search_type = "similarity",
    kwargs = {"k":2}
)


def docs_format(docs):
    context_text = " ".join(doc.page_content for doc in docs)
    return context_text

parallel_chain = RunnableParallel({
    'context' : retriever | RunnableLambda(docs_format),
    'question' : RunnablePassthrough()
})

parser = StrOutputParser()

final_chain = parallel_chain | prompt | llm | parser

while True:
    question = input("ask the question(type exit for quit) : ")
    if question == "exit":
        break
    

    result = final_chain.invoke(question)
    print("\n Answer : " , result)






