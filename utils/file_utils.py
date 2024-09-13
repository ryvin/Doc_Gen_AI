# utils/file_utils.py

import os
import logging
from typing import List
import PyPDF2
import docx

logger = logging.getLogger(__name__)

def parse_reference_files(directory: str, files: List[str]) -> str:
    """Parses reference files and returns their content.

    Args:
        directory: The directory containing the files.
        files: List of filenames to parse.

    Returns:
        A string containing the content of all reference files.
    """
    content = ""
    for file in files:
        filepath = os.path.join(directory, file)
        if file.lower().endswith('.pdf'):
            content += parse_pdf(filepath)
        elif file.lower().endswith('.docx'):
            content += parse_docx(filepath)
        elif file.lower().endswith('.txt') or file.lower().endswith('.md'):
            content += parse_txt(filepath)
        else:
            logger.warning("Unsupported file type: %s", file)
    return content

def parse_pdf(filepath: str) -> str:
    """Parses a PDF file and returns its text content.

    Args:
        filepath: Path to the PDF file.

    Returns:
        A string containing the text extracted from the PDF.
    """
    content = ""
    try:
        with open(filepath, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                content += page.extract_text()
    except Exception as e:
        logger.error("Failed to parse PDF file %s: %s", filepath, e)
    return content

def parse_docx(filepath: str) -> str:
    """Parses a DOCX file and returns its text content.

    Args:
        filepath: Path to the DOCX file.

    Returns:
        A string containing the text extracted from the DOCX.
    """
    content = ""
    try:
        doc = docx.Document(filepath)
        for para in doc.paragraphs:
            content += para.text + '\n'
    except Exception as e:
        logger.error("Failed to parse DOCX file %s: %s", filepath, e)
    return content

def parse_txt(filepath: str) -> str:
    """Reads a text file and returns its content.

    Args:
        filepath: Path to the text file.

    Returns:
        A string containing the content of the text file.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        logger.error("Failed to read text file %s: %s", filepath, e)
        return ""
