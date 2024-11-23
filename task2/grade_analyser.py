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
    # Ensure the output file is named exactly as {inputfilename}_out.csv
    base_name = os.path.basename(filename)
    output_file = os.path.splitext(base_name)[0] + "_out.csv"  # Keep only base name and add _out.csv

    try:
        with open(filename, 'r') as infile, open(output_file, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            # Read and skip the header row of the CSV file
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
                    writer.writerow([student_id, f"{average_grade:.2f}", classification])
                except ValueError:
                    print(f"Warning: Invalid data for student ID {student_id}, skipping this entry.")

        print(f"Data has been saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    input_filename = input("Enter the CSV file name: ").strip()
    process_student_data(input_filename)
