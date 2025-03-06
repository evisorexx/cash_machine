import pdfkit
import time
from pathlib import Path


def generate_pdf(html_content: str, output_folder: str = 'media'):
    Path(output_folder).mkdir(parents=True, exist_ok=True)  # Создадим директорию media, если она не существует.

    file_name = f"{int(time.time())}.pdf"
    output_path = Path(output_folder) / file_name

    try:
        pdfkit.from_string(html_content, str(output_path))
        return str(output_path)
    except Exception as e:
        raise Exception(f"Failed to generate PDF: {str(e)}")
