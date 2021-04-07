package multithread;

import java.util.Random;

public class MyTask implements Runnable {

    @Override
    public void run() {
        // TODO Auto-generated method stub
        int result;
        Random random = new Random(Thread.currentThread().getId());
        while (true) {
            result = 1000 / ((int) (random.nextDouble() * 1000000000));
            if (Thread.currentThread().isInterrupted()) {
                System.out.printf("%d : Interrupted\n", Thread.currentThread().getId());
                return;
            }
        }
    }

    public static void main(String[] args) {
        int numberOfThreads = 2 * Runtime.getRuntime().availableProcessors();
        MyThreadGroup myThreadGroup = new MyThreadGroup("MyThreadGroup");
        MyTask myTask = new MyTask();
        for (int i = 0; i < numberOfThreads; i++) {
            Thread t = new Thread(myThreadGroup, myTask);
            t.start();
        }
        System.out.printf("Number of Threads: %s\n", myThreadGroup.activeCount());
        System.out.printf("Information about the Thread Group\n");
        myThreadGroup.list();
        Thread[] threads = new Thread[myThreadGroup.activeCount()];
        myThreadGroup.enumerate(threads);
        for (int i = 0; i < myThreadGroup.activeCount(); i++) {
            System.out.printf("Thread %s: %s\n", threads[i].getName(), threads[i].getState());
        }
    }
    
}
