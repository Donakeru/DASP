public class BankGSTest {
  public static void main(String[] args) {
    Bank bank = new Bank();
    new Client("Client1", bank);
    new Client("Client2", bank);
    new Client("Client3", bank);
    new Client("Client4", bank);
    new Client("Client5", bank);
  }
}

class Bank {
  // Due to security measures, it has a maximum capacity of 3
  public static final int MAX_CAPACITY = 3;
  private int totalClientsInBank = 0;

  public synchronized void enter(String client) {
    while (totalClientsInBank >= MAX_CAPACITY) {
      try {
        System.out.println(" The bank is full " +
            client + " has to wait ");
        wait();
      } catch (InterruptedException e) {
        //
      }
    }
    // precondition is true
    System.out.println(client + " has entered");
    totalClientsInBank = totalClientsInBank + 1;
  }

  public synchronized void leave(String client) {
    totalClientsInBank = totalClientsInBank - 1;
    System.out.println(client +
        " has left, notify a waiting client");
    notify();
  }
}

class Client extends Thread {
  private Bank bank;
  private String name;

  Client(String n, Bank p) {
    name = n;
    bank = p;
    start();
  }

  public void run() {
    System.out.println(name + " is ready to enter");
    bank.enter(name);
    try {
      sleep(4000);
    } catch (InterruptedException e) {
      //
    }
    // leave after 4000ms
    bank.leave(name);
  }
}
