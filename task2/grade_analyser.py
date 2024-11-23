import csv
import os

def get_classification(average_grade):
    if average_grade >= 70:
        return "1"
    elif average_grade >= 60:
        return "2:1"
    elif average_grade >= 50:
        return "2:2"
    elif average_grade >= 40:
        return "3"
    else:
        return "F"

def process_student_data(filename):
    
    base_name = os.path.basename(filename) 
    output_file = os.path.splitext(base_name)[0] + "_out.csv"  

    try:
        with open(filename, 'r') as infile, open(output_file, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

        
            headers = next(reader)
            writer.writerow(["student_id", "average_grade", "classification"])

            for row in reader:
                student_id = row[0]
                try:
                    grades = [float(grade) for grade in row[1:] if grade.strip()]
                    if grades:
                        average_grade = sum(grades) / len(grades)
                    else:
                        average_grade = 0.0
                    classification = get_classification(average_grade)
                    writer.writerow([student_id, f"{average_grade:
