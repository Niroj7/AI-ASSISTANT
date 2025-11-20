import pdfplumber
import csv
import io

def process_file(uploaded_file):
    """
    Reads PDF, TXT, CSV files and returns extracted text.
    """

    file_type = uploaded_file.type.lower()

    # ------------------ PDF ------------------
    if "pdf" in file_type:
        try:
            with pdfplumber.open(uploaded_file) as pdf:
                text = ""
                for page in pdf.pages:
                    extracted = page.extract_text() or ""
                    text += extracted + "\n"
            return f"📄 PDF Extracted Text:\n\n{text}"
        except Exception as e:
            return f"❌ Could not read the PDF file.\n\nError: {str(e)}"

    # ------------------ TXT ------------------
    elif "text" in file_type:
        try:
            text = uploaded_file.read().decode("utf-8", errors="ignore")
            return f"📄 TXT File Content:\n\n{text}"
        except:
            return "❌ Could not read TXT file."

    # ------------------ CSV ------------------
    elif "csv" in file_type:
        try:
            string_io = io.StringIO(uploaded_file.read().decode("utf-8", errors="ignore"))
            reader = csv.reader(string_io)
            rows = list(reader)

            formatted = "\n".join([", ".join(row) for row in rows])
            return f"📊 CSV File Content:\n\n{formatted}"
        except Exception as e:
            return f"❌ Could not read the CSV file.\n\nError: {str(e)}"

    # ------------------ Unsupported ------------------
    else:
        return "❌ File format not supported. Upload PDF, TXT, or CSV."
