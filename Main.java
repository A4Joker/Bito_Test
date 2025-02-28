
// Main.java
public class Main {
    public static int globalVar = 42;
    public static int globalVar1 = 42;
    public static String globalVar2 = "Hello, World!";
    public static boolean globalVar3 = true;
    public static void main(String[] args) {
        ClassB classBInstance = new ClassB();
        classBInstance.useClassAStaticVar();
        System.out.println(globalVar); // changed line
    }
}
