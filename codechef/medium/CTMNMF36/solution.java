import java.util.Scanner;
class Codechef {
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        int a=s.nextInt();
        int i=1;
        while(i<=a){
            if(i%3==0 && i%5==0){
                System.out.println(i);
                
            }
            i++;
        }
        
    }
}