from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()


def main():
    print("Hello From Langchain!")
    information="""
    Hritik Rakesh Nagrath[1] (born 10 January 1974), known professionally as Hrithik Roshan (Hindi: [ˈɾɪt̪ɪk ɾoːʃən][2]), is an Indian actor and producer who works in Hindi cinema. Referred to as the millennial superstar,[3] he has portrayed a variety of characters and is known for his dancing skills. One of the highest-paid actors in India, he has won many awards, including six Filmfare Awards, of which four were for Best Actor. Starting from 2012, he has appeared in Forbes India's Celebrity 100 several times based on his income and popularity.

    Roshan has frequently collaborated with his father, Rakesh Roshan. He made brief appearances as a child actor in several films in the 1980s and later worked as an assistant director on four of his father's films. His first leading role was in the box-office success Kaho Naa... Pyaar Hai (2000), for which he received several awards. Performances in the 2000 terrorism drama Fiza and the 2001 ensemble family drama Kabhi Khushi Kabhie Gham consolidated his reputation but were followed by several poorly received films.
    """

    summary_template = """
    You are a summarization engine. Your task is to summarize the following information in 2 sentences.
    Information: {information}
    """

    summary_prompt = PromptTemplate.from_template(summary_template)

    llm = ChatGroq(model_name="llama-3.1-8b-instant", temperature=0.7)

    chain = summary_prompt | llm

    response = chain.invoke({"information": information})

    print(response.content)

if __name__ == "__main__":
    main()
