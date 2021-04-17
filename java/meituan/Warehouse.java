package meituan;

import java.util.Scanner;

public class Warehouse {

    public static int getWeight(int num, int[] goods) {
        int index = num - 1;
        goods[index] = 0;
        int weightLow = 0;
        int weightHigh = 0;
        for (int i = 0; i < goods.length; i++) {
            if (i < index) {
                weightLow += goods[i];
            }
            if (i > index) {
                weightHigh += goods[i];
            }
        }
        if (weightHigh >= weightLow) {
            return weightHigh;
        } else {
            return weightLow;
        }
    }

    public static void main(String[] args) throws Exception {
        try {
            Scanner scanner = new Scanner(System.in);
            String nextLine = scanner.nextLine();
            int size = Integer.parseInt(nextLine);
            int[] nums = new int[size];
            nextLine = scanner.nextLine();
            String[] numList = nextLine.split(" ");
            for (int i = 0; i < numList.length; i++) {
                nums[i] = Integer.parseInt(numList[i]);
            }
            int[] weights = new int[size];
            nextLine = scanner.nextLine();
            String[] weightList = nextLine.split(" ");
            for (int i = 0; i < numList.length; i++) {
                weights[i] = Integer.parseInt(weightList[i]);
            }
            for (int i = 0; i < weights.length; i++) {
                System.out.println(getWeight(weights[i], nums));
            }
        } catch (Exception e) {
            // TODO: handle exception
            throw new Exception("wrong input");
        }
    }
}
