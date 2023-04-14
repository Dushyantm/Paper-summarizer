from fpdf import FPDF


def save_results_to_file(results, filename):
    pdf = FPDF()
    
    pdf.set_font("Arial", size=12)
    for result in results:
        # Add a new page to the PDF
        pdf.add_page()
        print(result)
        # Add the result title to the PDF
        pdf.multi_cell(0, 10, result, border=0)

    pdf.output(filename)
    with open(filename, 'w') as f:
        for result in results:
            f.write(result)
            f.write('\n\n')

