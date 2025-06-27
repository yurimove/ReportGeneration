import csv
from fpdf import FPDF
import statistics

# Step 1: Read CSV data
def read_data(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [(row['Name'], int(row['Score'])) for row in reader]
    return data

# Step 2: Analyze data
def analyze_data(data):
    scores = [score for _, score in data]
    return {
        "average": round(statistics.mean(scores), 2),
        "highest": max(data, key=lambda x: x[1]),
        "lowest": min(data, key=lambda x: x[1])
    }

# Step 3: Generate PDF report
def generate_pdf(data, analysis, filename="report.pdf"):
    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Student Scores Report", ln=True, align='C')

    pdf.set_font("Arial", size=12)
    pdf.ln(10)

    # Table headers
    pdf.cell(60, 10, "Name", 1)
    pdf.cell(40, 10, "Score", 1)
    pdf.ln()

    # Table data
    for name, score in data:
        pdf.cell(60, 10, name, 1)
        pdf.cell(40, 10, str(score), 1)
        pdf.ln()

    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Summary", ln=True)

    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Average Score: {analysis['average']}", ln=True)
    pdf.cell(0, 10, f"Highest Score: {analysis['highest'][0]} ({analysis['highest'][1]})", ln=True)
    pdf.cell(0, 10, f"Lowest Score: {analysis['lowest'][0]} ({analysis['lowest'][1]})", ln=True)

    pdf.output(filename)
    print(f"PDF report generated: {filename}")

# Main
if __name__ == "__main__":
    data = read_data("data.csv")
    analysis = analyze_data(data)
    generate_pdf(data, analysis)
