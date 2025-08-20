def classify_question(q):
    if any(c.isdigit() for c in q) or any(op in q for op in ["+", "-", "*", "/"]):
        return "math"
    elif any(word in q.lower() for word in ["think", "feel", "opinion", "best", "should"]):
        return "opinion"
    else:
        return "factual"

def answer(q):
    cat = classify_question(q)
    if cat == "math":
        try:
            return "Math detected. Answer: " + str(eval(q))
        except:
            return "Math detected but could not evaluate."
    elif cat == "opinion":
        return "This looks like an opinion question."
    else:
        return "This looks like a factual question."

while True:
    q = input("Ask a question (or type 'exit'): ")
    if q == "exit":
        break
    print(answer(q))
