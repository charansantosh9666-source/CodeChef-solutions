import java.util.Scanner;

class Codechef {
    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        
        boolean bookingStatus = sc.nextBoolean();
        String roomType = sc.next();


            // Nested if condition checks the type of room
        if(bookingStatus==true){
            if(roomType.equals("Luxury")){
                System.out.println("Welcome to your Luxury Suite!");
            }else {
                System.out.println("Welcome to your Standard Room!");
            }
        } else {
            System.out.println("Booking not found. Please check your details.");
        }

        // Indicating that the reservation check is completed
        System.out.println("Reservation check completed.");
    }
}
