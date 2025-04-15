from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rag_chain import get_rag_chain

app = FastAPI()


class Question(BaseModel):
    question: str
    model_name: str = "mistral-nemo:latest"

@app.post("/ask")
def question_answer(question: Question):
    try:

        qa_chain = get_rag_chain(question.model_name)
        result = qa_chain({"query": question.question})
        answer = result["result"]
        source = result["source_documents"]

        source_info = "\n".join(
            f"📄 Source: {doc.metadata.get('source', 'Unknown')} (Page: {doc.metadata.get('page', 'N/A')})"
            for doc in source   
        )

        final_result = {"answer":answer, "sources": source_info}
        print(final_result)

        return final_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))