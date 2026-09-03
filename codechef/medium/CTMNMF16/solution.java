import java.util.*;

class Codechef {
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in); // Create a Scanner object for input
        
        // Ask the user to enter the initial water level
        // Read the user input as a double value
        float a= scanner.nextFloat();
        
        
        // Start while loop to decrease water leve
        while(a>10){
            
                System.out.println("Water level: "+a+" liters");
            
            a--;
        }
        
        // Alert user when only 10 liters remain
        System.out.println("Warning! Water level is low (10 liters). Please refill the tank!");
        
        scanner.close(); // Close the Scanner
    }
}