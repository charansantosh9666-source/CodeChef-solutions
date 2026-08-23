import java.util.Scanner; // Import the Scanner class to read input from the user

class Codechef {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Create a Scanner object for taking user input

        // Prompt the user to enter the hour of the day (0 to 23)
        int hour = scanner.nextInt(); // Read the input value as an integer
        
        // Check if the hour is between 5 and 11 inclusive (morning time)
        if (hour >= 5 && hour <= 11) {
            System.out.println("Good morning!"); // Print morning greeting
        }else if(hour >= 12 && hour <= 17){
            System.out.println("Good afternoon!");
        }else if(hour >= 18 && hour <= 21){
            System.out.println("Good evening!");
        }else if(hour >= 22 && hour <= 23){
            System.out.println("Good night!");
        }else if (hour > 23 || hour < 0){
            System.out.println("Invalid hour entered");
        }

        scanner.close(); // Close the Scanner object to prevent resource leaks
    }
}
