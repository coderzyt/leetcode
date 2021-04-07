package multithread;

import java.util.Date;
import java.util.concurrent.TimeUnit;

public class UnsafeTask implements Runnable {

    private Date startDate;

    @Override
    public void run() {
        // TODO Auto-generated method stub
        startDate = new Date();
        System.out.printf("Starting thread: %s: %s\n", Thread.currentThread().getId(), startDate);
        try {
            TimeUnit.SECONDS.sleep((int) Math.rint(Math.random() * 10));
        } catch (InterruptedException e) {
            //TODO: handle exception
            e.printStackTrace();
        }
        System.out.printf("Thread Finished: %s: %s\n", Thread.currentThread().getId(), startDate);
    }

    public static void main(String[] args) {
        for (int i = 0; i < 10; i++) {
            UnsafeTask unsafeTask = new UnsafeTask();
            Thread thread = new Thread(unsafeTask);
            thread.start();
            try {
                TimeUnit.SECONDS.sleep(2);
            } catch (InterruptedException e) {
                //TODO: handle exception
                e.printStackTrace();
            }
        }
    }
    
}
