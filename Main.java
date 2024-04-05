/* IMPORTANT: class must not be public. */

/*
 * uncomment this if you want to read input.
import java.io.BufferedReader;
import java.io.InputStreamReader;
*/
import java.io.*;
import java.util.Scanner;
class Main {
    public static void main(String args[] ) throws Exception {
        /*
         * Read input from stdin and provide input before running

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        int N = Integer.parseInt(line);
        for (int i = 0; i < N; i++) {
            System.out.println("hello world");
        }
        */
int num;
        Scanner s = new Scanner(System.in);
 
        // Read the next integer from the screen
        num = s.nextInt();
 
        // Display the integer
        System.out.println("Entered integer is: "
                           + num);
    }
}