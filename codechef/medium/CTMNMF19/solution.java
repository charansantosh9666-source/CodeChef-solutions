import java.util.*;
class Codechef {
    public static void main(String[] args) {
        Scanner s= new Scanner(System.in);
        //Take input of n from user
        int n= s.nextInt();
        
        int number = 2; // Starting with the first even number
        
        System.out.println("Even numbers from 2 to " + n + ":");
        
        while (number <= n) {  // Continue loop until number is less than or equal to n
            if(number%2==0){
                System.out.println(number);
                
            }
            number++;
        }
    }
}

