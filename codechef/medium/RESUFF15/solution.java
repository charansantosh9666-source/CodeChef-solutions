import java.util.Scanner; 

class Codechef {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); 
        double weight = scanner.nextDouble(); 
        scanner.nextLine(); 
        String deliverySpeed = scanner.nextLine(); 
        if(weight <= 5.){
            if(deliverySpeed.equals("Express")){
                System.out.println("Shipping charge: $15");
            }else{
                System.out.println("Shipping charge: $10");
            }
        }else{
            System.out.println("Shipping not available for packages above 5 kg.");
        }
        scanner.close(); 
    }
}
