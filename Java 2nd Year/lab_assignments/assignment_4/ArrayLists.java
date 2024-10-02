//122318693 Program 1

import java.util.Scanner;
import java.util.ArrayList;

public class ArrayLists {
    public static void main(String[] args) {
        ArrayList<String> ComSciModules = new ArrayList<>();
        Scanner scan = new Scanner(System.in);
        System.out.println("Please enter the number of modules you wish to enter: ");
        int mod_count = scan.nextInt();
        scan.nextLine();

        for (int i = 0; i < mod_count; i++) {
            System.out.println("Enter the module name: ");
            ComSciModules.add(scan.nextLine());
        }
        scan.close();

        for (int i = 0; i < ComSciModules.size(); i++) {
            if ((ComSciModules.get(i).toLowerCase()).equals("networking")) {
                ComSciModules.remove(i);
            }
        }

        int n = ComSciModules.size();
        for (int i = 0; i < n - 1; i++) {
            for (int j =0; j < n - i - 1; j++) {
                if (ComSciModules.get(j).compareTo(ComSciModules.get(j + 1)) < 0) {
                    //Swap the list element j and element j + 1
                    String temp = ComSciModules.get(j);
                    ComSciModules.set(j, ComSciModules.get(j + 1));
                    ComSciModules.set(j + 1, temp);
                }
            }
        }
        System.out.println("Reverse order:");
        for (int i = 0; i <= ComSciModules.size() - 1; i++) {
            System.out.println(ComSciModules.get(i));
        }
    }
}