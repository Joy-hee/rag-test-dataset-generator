import os
import sys
import logging
from document_processor import DocumentProcessor
from question_generator import QuestionGenerator
from output_formatter import OutputFormatter

def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    try:
        # Initialize components
        doc_processor = DocumentProcessor()
        question_generator = QuestionGenerator()
        output_formatter = OutputFormatter()

        # Example paths for input and output
        input_path = 'data/documents'
        output_path = 'output/'

        # Process documents
        documents = doc_processor.load_documents(input_path)
        for doc in documents:
            logger.info(f'Processing document: {doc}')
            questions = question_generator.generate_questions(doc)
            logger.info(f'Generated questions for {doc}: {questions}')
            output_formatter.format_output(questions, output_path)

        logger.info('All documents processed successfully.')

    except Exception as e:
        logger.error(f'An error occurred: {e}')
        sys.exit(1)

if __name__ == "__main__":
    main()
