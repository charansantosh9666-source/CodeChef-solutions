import java.util.Scanner; // Import Scanner class to take input from the user

class Codechef {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Create a Scanner object for user input
        
        // Read user input and store it in the 'temperature' variable
        int t=scanner.nextInt();
        if(t>30){
            System.out.println("It's hot outside! Stay hydrated.");
        }
        else if(t<=30 && t>=10){
            System.out.println("The weather is moderate. Enjoy your day!");
        }else{
            System.out.println("It's cold outside! Wear warm clothes.");
        }
        scanner.close(); 
    }
}
