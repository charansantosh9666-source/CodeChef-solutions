import java.util.Scanner; // Import Scanner class for taking input from the user

class Codechef {
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in); // Create a Scanner object for user input

        // Read the marks input from the user
        int marks = scanner.nextInt(); 
        String grade="";
        if(marks>=90){
            grade="A+";
        }else if (marks>=80 && marks<90){
            grade="A";
        }else if(marks>=70 && marks<80){
            grade="B";
        }else if(marks>=60 && marks<70){
            grade="C";
        }else if(marks<60){
            grade="Fail";
        }
        System.out.println("The grade is: " +grade);

        scanner.close(); // Close the Scanner object to free up resources
    }
}
