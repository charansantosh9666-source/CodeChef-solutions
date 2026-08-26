import java.util.Scanner;  

class Codechef {  
    public static void main(String[] args) {
        
        // Create a Scanner object to read input from the user
        Scanner scanner = new Scanner(System.in);  
        
        // Read an integer input from the user
        int number = scanner.nextInt();  
        int sum=0;
        while(number>0){
            sum+=number%10;
            number/=10;
        }

        // Print the result, which is the sum of the digits
        System.out.println("Sum of digits: " + sum);
    }  
}