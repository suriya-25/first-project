# Student Marks Analyzer Project
def get_marks():
    subjects = []
    marks = []
    n = int(input("Enter number of subjects: "))
    for i in range(n):
        sub = input(f"Enter subject {i+1} name: ")
        mark = float(input(f"Enter marks for {sub}: "))
        subjects.append(sub)
        marks.append(mark)
    return subjects, marks
def analyze_marks(subjects, marks):
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)
    high_sub = subjects[marks.index(highest)]
    low_sub = subjects[marks.index(lowest)]
    return total, average, (highest, high_sub), (lowest, low_sub)
def grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"
def main():
    subjects, marks = get_marks()
    total, average, highest, lowest = analyze_marks(subjects, marks)
    print("\n----- Report Summary -----")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Highest Marks: {highest[0]} in {highest[1]}")
    print(f"Lowest Marks: {lowest[0]} in {lowest[1]}")
    print(f"Overall Grade: {grade(average)}")
    print("\nReport Generated Successfully!")
if __name__ == "__main__":
    main()
