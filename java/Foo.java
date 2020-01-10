class Foo {

    private CountDownLatch c1;

    private CountDownLatch c2;

    public Foo() {
        this.c1 = new CountDownLatch(1);
        this.c2 = new CountDownLatch(1);
    }

    public void first() {
        System.out.print("one");
        c1.countdown();
    }

    public void second() {
        c1.await();
        System.out.print("two");
        c2.countdown();
    }

    public void third() {
        c2.await();
        System.out.print("three");
    }


    public static void main(String[] args) {
        Foo foo = new Foo();
        foo.first();
    }


}