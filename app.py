from flask import Flask, render_template, request, send_file
import os
import sys

# Add GTK3 bin directory to the PATH
os.environ['PATH'] += r';C:\Program Files\GTK3-Runtime Win64\bin'

# Try importing WeasyPrint
try:
    from weasyprint import HTML
except Exception as e:
    print(f"Error importing WeasyPrint: {e}")
    sys.exit(1)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/form', methods=['POST'])
def form():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    summary = request.form['summary']

    education_high = {
        "name": request.form['education_high'],
        "location": request.form['location_high'],
        "date": request.form['date_high'],
        "percentage": request.form['percentage_high'],
    }

    education_inter = {
        "name": request.form['education_inter'],
        "location": request.form['location_inter'],
        "date": request.form['date_inter'],
        "percentage": request.form['percentage_inter'],
    }

    education_ssc = {
        "name": request.form['education_ssc'],
        "location": request.form['location_ssc'],
        "date": request.form['date_ssc'],
        "percentage": request.form['percentage_ssc'],
    }

    internships = request.form['internships']
    projects = request.form['projects']
    certifications = request.form['certifications']

    # Render the resume HTML
    resume_html = render_template('resume.html', name=name, phone=phone, email=email, summary=summary,
                                   education_high=education_high, education_inter=education_inter,
                                   education_ssc=education_ssc, internships=internships,
                                   projects=projects, certifications=certifications)

    # Convert the HTML to PDF
    pdf = HTML(string=resume_html).write_pdf()

    # Save the PDF to a file
    pdf_path = 'resume.pdf'  # Change the filename as needed
    with open(pdf_path, 'wb') as f:
        f.write(pdf)

    return f"Resume generated successfully! You can download it <a href='/download'>here</a>."

@app.route('/download')
def download_file():
    return send_file('resume.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
