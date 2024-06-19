from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def gpt3(question):
    llm = ChatOpenAI(temperature=0.9, model_name="gpt-3.5-turbo-0613")
    
    prompt = PromptTemplate(template="{question}", input_variables=["question"])

    llm_chain = LLMChain(prompt=prompt, llm=llm)
    
    response = llm_chain.invoke({"question": question})
    
    return response["text"]

def gpt4(question, temperature=0.9):
    llm = ChatOpenAI(temperature=temperature, model_name="gpt-4-0613")
    
    prompt = PromptTemplate(template="{question}", input_variables=["question"])

    llm_chain = LLMChain(prompt=prompt, llm=llm)
    
    response = llm_chain.invoke({"question": question})
    
    return response["text"]
