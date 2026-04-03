import os
import pdfplumber
from bs4 import BeautifulSoup

class DocumentProcessor:
    def __init__(self):
        self.metadata = {}

    def parse_html(self, file_path):
        """Parse HTML file and extract text with structure information."""
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            self.metadata['title'] = soup.title.string if soup.title else 'Untitled'
            self.metadata['sections'] = self._extract_sections(soup)
            self.metadata['page_numbers'] = self._extract_page_numbers(soup)
            return self.metadata

    def parse_pdf(self, file_path):
        """Parse PDF file and extract text with structure information."""
        with pdfplumber.open(file_path) as pdf:
            self.metadata['title'] = os.path.basename(file_path)
            self.metadata['sections'] = []
            self.metadata['page_numbers'] = []
            for i, page in enumerate(pdf.pages):
                text = page.extract_text() or ''
                self.metadata['sections'].append({'page': i + 1, 'text': text})
                self.metadata['page_numbers'].append(i + 1)
            return self.metadata

    def _extract_sections(self, soup):
        """Extract sections information from HTML soup."""
        sections = []
        for section in soup.find_all(['h1', 'h2', 'h3']):
            sections.append({'heading': section.name, 'text': section.get_text()})
        return sections

    def _extract_page_numbers(self, soup):
        """Placeholder for page number extraction logic from HTML soup."""
        return []  # This might depend on your specific needs and HTML structure.
