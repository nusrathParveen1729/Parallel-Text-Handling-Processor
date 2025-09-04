import multitasking
from sentiment_analysis import score_paragraph

results = {}

@multitasking.task
def process_paragraph(i, chunk):
    score = score_paragraph(chunk)
    results[i] = score   # store results with index

if __name__ == "__main__":
    # Read file
    with open("randomparas.txt", "r",encoding ="utf-8") as f:
        huge_text = f.read()

    # Split into paragraphs
    chunks = huge_text.split("\n")

    # Run sentiment scoring concurrently
    for i, chunk in enumerate(chunks):
        process_paragraph(i, chunk)

    # Wait for all tasks to finish
    multitasking.wait_for_tasks()

    # Print results in order
    for i in range(len(chunks)):
        print(f"Para{i}, Score is {results[i]}")
