package multithread;

import java.io.File;
import java.util.concurrent.TimeUnit;

public class FileSearch implements Runnable {

    private String initPath;

    private String fileName;

    public FileSearch(String initPath, String fileName) {
        this.initPath = initPath;
        this.fileName = fileName;
    }

    @Override
    public void run() {
        // TODO Auto-generated method stub
        File file = new File(initPath);
        if (file.isDirectory()) {
            try {
                directoryProcess(file);
            } catch (InterruptedException e) {
                //TODO: handle exception
                System.out.printf("%s: The search has been interrupted", Thread.currentThread().getName());
            }
        }
    }

    private void directoryProcess(File file) throws InterruptedException {
        File list[] = file.listFiles();
        if (list != null) {

            for (int i = 0; i < list.length; i++) {
                if (list[i].isDirectory()) {
                    directoryProcess(list[i]);
                } else {
                    fileProcess(list[i]);
                }
            }
            if (Thread.interrupted()) {
                throw new InterruptedException();
            }
        }
    }

    private void fileProcess(File file) throws InterruptedException {
        if (file.getName().equals(fileName)) {
            System.out.printf("%s: %s\n", Thread.currentThread().getName(), file.getAbsolutePath());
        }
        if (Thread.interrupted()) {
            throw new InterruptedException();
        }
    }
    
    public static void main(String[] args) {
        FileSearch fileSearch = new FileSearch("/Users/clay/Downloads/project", "DemoController.java");
        Thread thread = new Thread(fileSearch);
        thread.start();
        try {
            TimeUnit.SECONDS.sleep(1);
        } catch (InterruptedException e) {
            //TODO: handle exception
            e.printStackTrace();
        }
        thread.interrupt();
    }
}
