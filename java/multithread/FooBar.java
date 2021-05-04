import java.util.concurrent.Semaphore;

class FooBar {
    private int n;

    public FooBar(int n) {
        this.n = n;
    }
    
    

    private Semaphore semaphore = new Semaphore(1);
    private Semaphore semaphore2 = new Semaphore(0);

    public void foo(Runnable printFoo) throws InterruptedException {

        for (int i = 0; i < n; i++) {
            semaphore.acquire();

            // printFoo.run() outputs "foo". Do not change or remove this line.
            printFoo.run();
            semaphore2.release();
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {

        for (int i = 0; i < n; i++) {
            semaphore2.acquire();
            // printBar.run() outputs "bar". Do not change or remove this line.
            printBar.run();
            semaphore.release();
        }
    }

    public static void main(String[] args) {
        FooBar fooBar = new FooBar(10);
        Runnable printFoo = new Runnable() {
            @Override
            public void run() {
                System.out.print("Foo");
            }
        };

        Runnable printBar = new Runnable() {
            @Override
            public void run() {
                System.out.print("Bar");
            }
        };
        Thread foo = new Thread(new Runnable(){
            @Override
            public void run() {
                try {
                    fooBar.foo(printFoo);
                } catch (InterruptedException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
            }
        });
        Thread bar = new Thread(new Runnable(){
            @Override
            public void run() {
                try {
                    fooBar.bar(printBar);
                } catch (InterruptedException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
            }
        });
        foo.start();
        bar.start();
    }
}