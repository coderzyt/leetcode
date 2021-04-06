package multithread;

public class PrimeGenerator extends Thread {

    private boolean isPrime(long number) {
        if (number <= 2) {
            return true;
        }
        for (long i = 2; i < number; i++) {
            if (number % i == 0) {
                return false;
            }
            return true;
        }
        return false;
    }
    
    @Override
    public void run() {
        long number = 1L;
        while (true) {
            if (isPrime(number)) {
                System.out.printf("Number %d is Prime\n", number);
            }
            if (isInterrupted()) {
                System.out.println("The Prime Generator has been interrupted");
                return;
            }
            number++;
        }
    }

    public static void main(String[] args) {
        Thread task = new PrimeGenerator();
        task.start();
        try {
            Thread.sleep(5000);
        } catch (Exception e) {
            e.printStackTrace();
            //TODO: handle exception
        }
        task.interrupt();
        // try {
        //     Thread.sleep(1000);
        // } catch (Exception e) {
        //     e.printStackTrace();
        //     //TODO: handle exception
        // }
        System.out.printf("Main: Status of the Thread: %s\n", task.getState());
        System.out.printf("Main: is Interrupted: %s\n", task.isInterrupted());
        System.out.printf("Main: is Alive: %s\n", task.isAlive());
    }
}
