import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Username {

    public static String getUserName(String username) {
        char prefix = username.charAt(0);
        boolean low = (prefix - 'a') >= 0 && (prefix - 'a') <= 25;
        boolean high = (prefix - 'A') >= 0 && (prefix - 'A') <= 25;
        int numberNum = 0;
        int characterNum = 0;
        if (low || high) {
            for (int i = 0; i < username.length(); i++) {
                char ch = username.charAt(i);
                boolean lowi = (ch - 'a') >= 0 && (ch - 'a') <= 25;
                boolean highi = (ch - 'A') >= 0 && (ch - 'A') <= 25;
                boolean numi = (ch - '0' >= 0) && ((ch - '0') <= 9);
                if (lowi || highi) {
                    characterNum++;
                }
                if (numi) {
                    numberNum++;
                }
            }
            if (numberNum + characterNum == username.length()) {
                if (numberNum >= 1 && characterNum >= 1){
                    return "Accept";
                }
            }
        }
        return "Wrong";
    }

    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        int num = 0;
        LinkedList<String> strings = new LinkedList<>();
        String nextLine = scanner.nextLine();
        try {
            num = Integer.parseInt(nextLine);
        } catch (Exception e) {
            //TODO: handle exception
            throw new Exception("wrong input");
        }

        while (num > 0) {
            nextLine = scanner.nextLine();
            num--;
            strings.add(nextLine);
        }

        for (int i = 0; i < strings.size(); i++) {
            System.out.println(getUserName(strings.get(i)));
        }
    }
}
