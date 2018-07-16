import java.util.Scanner;

class money
{
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        System.out.println("Enter Rs:");
        double rs=s.nextDouble();
        double dollar = (rs/60);
        System.out.println("Rs "+ rs +" = Dollar " + dollar);
    }
}