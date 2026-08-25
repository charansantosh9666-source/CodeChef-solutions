import java.util.Scanner; // Import Scanner class for user input

class Codechef {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Create Scanner object for input

        // Display menu options
        System.out.println("Welcome to the Restaurant! Please select a dish:");
        System.out.println("1. Pasta");
        System.out.println("2. Burger");
        System.out.println("3. Salad");
        System.out.println("4. Dessert");

        // Read user input for menu choice
        int choice = scanner.nextInt();
        String dish="";
        if(choice==1){
            dish="Pasta";
        }else if(choice==2){
            dish="Burger";
        }else if(choice==3){
            dish="Salad";
        }else if(choice==4){
            dish="Dessert";
        }else{
            dish="Invalid";
        }
        System.out.println("You selected: " + dish);

        scanner.close(); // Close the Scanner object
    }
}
