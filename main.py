from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama


def main():
    information = """
    Elon Reeve Musk (born June 28, 1971) is a businessman known for his work in technology, transportation, and space exploration. Born in Pretoria, South Africa, he moved to Canada before attending the University of Pennsylvania in the United States.

Musk co-founded Zip2, an online city guide software company, and later X.com, an online financial services company that eventually became PayPal. After PayPal was acquired by eBay in 2002, Musk used much of the proceeds to invest in new ventures.

He founded SpaceX in 2002 with the goal of reducing the cost of space transportation and enabling the colonization of Mars. Under his leadership, SpaceX developed the Falcon rockets, Dragon spacecraft, and the reusable rocket system, significantly reducing the cost of launching payloads into space.

Musk joined Tesla Motors in 2004 as an investor and later became its CEO and product architect. Tesla became one of the world's leading electric vehicle manufacturers, producing vehicles such as the Model S, Model 3, Model X, and Model Y. The company also expanded into battery storage and solar energy products.

In addition to SpaceX and Tesla, Musk founded The Boring Company, which focuses on tunnel construction and transportation infrastructure. He also co-founded Neuralink, a company developing brain-computer interfaces, and xAI, an artificial intelligence company.

In 2022, Musk acquired Twitter, later renaming the platform to X. His leadership and business decisions have attracted significant public attention, making him one of the most influential and controversial entrepreneurs of the modern era.
    """

    summary_template = """
You are an expert text summarizer.

Summarize the following information in 4-5 concise sentences.

Information:
{information}
"""

    prompt = PromptTemplate.from_template(summary_template)

    llm = ChatOllama(
        model="gemma3:270m",
        temperature=0,
    )

    chain = prompt | llm

    response = chain.invoke({"information": information})

    print(response.content)


if __name__ == "__main__":
    main()
