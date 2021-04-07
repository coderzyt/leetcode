package multithread;

public class Task implements Runnable {

    @Override
    public void run() {
        // TODO Auto-generated method stub
        int numero = Integer.parseInt("TTT");
    }

    public static void main(String[] args) {
        Task task = new Task();
        Thread thread = new Thread(task);
        thread.setUncaughtExceptionHandler(new ExceptionHandler());
        thread.start();
    }
    
}
