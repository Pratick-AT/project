from transformers import pipeline

def answer_question(question, context):
    qa_pipeline = pipeline("question-answering")
    result = qa_pipeline(question=question, context=context)
    return result["answer"]
