interface P1
{
    double var1=5;
    void display1();
}

interface P2
{
    double var2=10;
    void display2();
}

interface P extends P1,P2
{
    double var=15;
    void display();
}

interface P12 extends P
{
    double var12=20;
    void display12();
}

class Q implements P12
{
    public void display1()
    {
        System.out.println("P1 Constant= "+var1);
    }
    public void display2()
    {
        System.out.println("P2 Constant= "+var2);
    }
    public void display12()
    {
        System.out.println("P12 Constant= "+var12);
    }
    public void display()
    {
        System.out.println("P Constant= "+var);
    }
}

class DemoP
{
    public static void main(String[] args) {
        Q q=new Q();
        q.display();
        q.display1();
        q.display12();
        q.display2();
    }
}