from data_processor import ingest_and_embed_pdf

pdf_path = "sample.pdf"

try:
    retriever = ingest_and_embed_pdf(pdf_path)

    results = retriever.invoke(
        "What is the main topic of this document?"
    )

    print("\nRetrieved document content:\n")

    for index, document in enumerate(results, start=1):
        print(f"--- Result {index} ---")
        print(document.page_content[:500])
        print("Page metadata:", document.metadata)
        print()

except Exception as error:
    print(f"Test failed: {error}")