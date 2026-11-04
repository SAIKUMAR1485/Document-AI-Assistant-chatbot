from openai import OpenAI

from config import OPENAI_API_KEY, OPENAI_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)


def ask_question(question, vector_store_id):

    response = client.responses.create(

        model=OPENAI_MODEL,

        instructions="""

        You are an AI Document Assistant.

        Your responsibility is to answer questions
        based ONLY on the uploaded documents.

        RULES:

        1. Use information from the uploaded documents.
        2. Do not use your general knowledge.
        3. Do not make up information.
        4. If the answer is not available in the
           document, say:

           "Sorry, I couldn't find this information
           in the uploaded document."

        5. Give clear and understandable answers.
        6. Use bullet points when necessary.

        """,

        input=question,

        tools=[
            {
                "type": "file_search",

                "vector_store_ids": [
                    vector_store_id
                ],

                "max_num_results": 5
            }
        ]
    )

    return response.output_text