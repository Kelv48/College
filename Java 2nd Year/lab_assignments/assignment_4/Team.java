//122318693 Program 2
import java.util.HashMap;
import java.util.Scanner;


public class Team {
    public static void main(String args[]) {
        HashMap<Integer, String> players = new HashMap<Integer, String>();

        //add 18 players to the map (kit number, Name)
        players.put(1, "Name1");
        players.put(2, "Name2");
        players.put(3, "Name3");
        players.put(4, "Name4");
        players.put(5, "Name5");
        players.put(6, "Name6");
        players.put(7, "Name7");
        players.put(8, "Name8");
        players.put(9, "Name9");
        players.put(10, "Name10");
        players.put(11, "Name11");
        players.put(12, "Name12");
        players.put(13, "Name13");
        players.put(14, "Name14");
        players.put(15, "Name15");
        players.put(16, "Name16");
        players.put(17, "Name17");
        players.put(18, "Name18");

        Scanner scan = new Scanner(System.in);
        System.out.println("Enter the jersey number to see if they are on the team: ");
        int jersey_num = scan.nextInt();
        scan.nextLine();

        String player_name = players.get(jersey_num);

        if(player_name != null) {
            System.out.println("Player name " + player_name);
            System.out.println("Player number " + jersey_num);
        } else {
            System.out.println("The club doesn't have a player with this number: " + jersey_num);
        }
        scan.close();
    }
}
