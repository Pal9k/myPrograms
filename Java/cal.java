import java.util.Scanner;

import javax.swing.plaf.synth.SynthEditorPaneUI;

class cal 
{
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        System.out.print("Enter num1:");
        double num1=s.nextDouble();
        System.out.print("Enter num2:");
        double num2=s.nextDouble();
        System.out.println("1.Addition");
        System.out.println("2.Subtraction");
        System.out.println("3.Multiplication");
        System.out.println("4.Division");
        System.out.print("Enter your choise:");
        int choise=s.nextInt();

        switch(choise)
        {
            case 1:System.out.println("Addition = "+(num1+num2));
                    break;
            case 2:System.out.println("Suntraction = "+(num1-num2));
                    break;
            case 3:System.out.println("Multiplication = "+(num1*num2));
                    break;
            case 4:System.out.println("Division = "+(num1/num2));
                    break;
        }
    }
}