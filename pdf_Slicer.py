##Edit PDF_NAME and SPLITS##
#Document needs to me in the same folder as code

from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

# === CONFIG ===
PDF_NAME = "contrato.pdf"  # file name
SPLITS = [
    (1, 1),
    (2, 2),
    (3, 15),
    (16, 18),
    (19, 23),
]
# ==============

# Check file existence
pdf_path = Path(PDF_NAME)
if not pdf_path.exists():
    raise FileNotFoundError(f"Could not find '{PDF_NAME}' on your Desktop.")

# Open the PDF
reader = PdfReader(str(pdf_path))
num_pages = len(reader.pages)
print(f"Opened {PDF_NAME} with {num_pages} pages.")

# Split and export each range
for i, (start, end) in enumerate(SPLITS, 1):
    if start < 1 or end > num_pages or start > end:
        raise ValueError(f"Invalid range {start}-{end} for a {num_pages}-page PDF.")
    writer = PdfWriter()
    for p in range(start - 1, end):  # PyPDF2 uses 0-indexing
        writer.add_page(reader.pages[p])

    out_name = f"pages_{start}-{end}.pdf"
    with open(out_name, "wb") as f:
        writer.write(f)
    print(f"✅ Created {out_name}")

print("Done!")