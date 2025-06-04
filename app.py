from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            current_cgpa = float(request.form['current_cgpa'])
            credits_completed = float(request.form['credits_completed'])
            course_completed = credits_completed / 3

            repeated = request.form.get('repeated') == 'yes'
            repeated_gpa = float(request.form['repeated_gpa']) if repeated else 0
            new_repeated_gpa = float(request.form['new_repeated_gpa']) if repeated else 0

            new_courses = int(request.form['new_courses'])
            new_gpa_list = [float(gpa) for gpa in request.form.getlist('new_gpas')]

            new_gpa_total = sum(new_gpa_list)
            old_total = ((current_cgpa * credits_completed) / 3) - repeated_gpa + new_repeated_gpa
            updated_cgpa = (old_total + new_gpa_total) / (course_completed + new_courses)
            total_course_completed = course_completed + new_courses
            result = {
                'updated_cgpa': round(updated_cgpa, 3),
                'course_completed': round(total_course_completed, 2),
                'new_courses': new_courses,
                'repeated': repeated,
                'repeated_gpa': repeated_gpa,
                'new_repeated_gpa': new_repeated_gpa
            }

        except Exception as e:
            result = {'error': 'Invalid input. Please check your entries.'}

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
