import java.util.Scanner;
import java.util.Vector;

class Student {
    private String name;

    public Student(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}

public class StudentVector {
    public static void main(String[] args) {
        Vector<Student> students = new Vector<>();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Menu:");
            System.out.println("1. Add Student name");
            System.out.println("2. Remove Student name");
            System.out.println("3. Search student by index");
            System.out.println("4. Display contents of the vector");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter the student name: ");
                    scanner.nextLine(); // Consume newline
                    String name = scanner.nextLine();
                    students.add(new Student(name));
                    System.out.println("Student added successfully.");
                    break;
                case 2:
                    System.out.print("Enter the student name to remove: ");
                    scanner.nextLine(); // Consume newline
                    String removeName = scanner.nextLine();
                    boolean removed = false;

                    for (Student student : students) {
                        if (student.getName().equals(removeName)) {
                            students.remove(student);
                            removed = true;
                            System.out.println("Student removed successfully.");
                            break;
                        }
                    }

                    if (!removed) {
                        System.out.println("Student not found in the vector.");
                    }
                    break;
                case 3:
                    System.out.print("Enter the index of the student to search: ");
                    int index = scanner.nextInt();
                    if (index >= 0 && index < students.size()) {
                        Student student = students.get(index);
                        System.out.println("Student found at index " + index + ": " + student.getName());
                    } else {
                        System.out.println("Invalid index.");
                    }
                    break;
                case 4:
                    System.out.println("Contents of the vector:");
                    for (Student student : students) {
                        System.out.println(student.getName());
                    }
                    break;
                case 5:
                    System.out.println("Exiting the program.");
                    System.exit(0);
                default:
                    System.out.println("Invalid choice. Please try again.");
            }

            System.out.println();
        }
    }
}