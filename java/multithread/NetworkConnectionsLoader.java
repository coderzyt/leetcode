package multithread;

import java.util.Date;
import java.util.concurrent.TimeUnit;

public class NetworkConnectionsLoader implements Runnable {

    @Override
    public void run() {
        // TODO Auto-generated method stub
        System.out.printf("Begin network connections loading: %s\n", new Date());
        try {
            TimeUnit.SECONDS.sleep(6);
        } catch (InterruptedException e) {
            //TODO: handle exception
            e.printStackTrace();
        }
        System.out.printf("Network connections loading has finished: %s\n", new Date());
    }
    
}
