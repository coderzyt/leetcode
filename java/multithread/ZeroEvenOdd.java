import java.util.concurrent.Semaphore;

class ZeroEvenOdd {
    private int n;

    public ZeroEvenOdd(int n) {
        this.n = n;
    }

    Semaphore semaphore0 = new Semaphore(1);
    Semaphore semaphore1 = new Semaphore(0);
    Semaphore semaphore2 = new Semaphore(0);

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void zero(IntConsumer printNumber) throws InterruptedException {

    }

    public void even(IntConsumer printNumber) throws InterruptedException {

    }

    public void odd(IntConsumer printNumber) throws InterruptedException {

    }

    public static void main(String[] args) {
        ZeroEvenOdd zeroEvenOdd = new ZeroEvenOdd(10);

    }
}