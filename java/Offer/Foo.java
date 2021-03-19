package Offer;

import java.util.concurrent.Semaphore;
import java.util.concurrent.locks.ReentrantLock;

class Foo {

    public Foo() {
        object1 = new Semaphore(0);
        object2 = new Semaphore(0);
    }

    public Semaphore object1;
    public Semaphore object2;

    public void first(Runnable printFirst) throws InterruptedException {

        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();

        object1.release();

    }

    public void second(Runnable printSecond) throws InterruptedException {

        object1.acquire();

        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();

        object2.release();
    }

    public void third(Runnable printThird) throws InterruptedException {

        object2.acquire();
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
    }
}
