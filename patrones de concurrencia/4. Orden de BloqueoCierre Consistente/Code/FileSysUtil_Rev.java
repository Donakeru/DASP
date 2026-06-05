public class FileSysUtil_Rev {

  public void moveContents(Directory src, Directory dest) {
    if (src.hashCode() > dest.hashCode()) {
      synchronized (src) {
        synchronized (dest) {
          System.out.println("Contents Moved Successfully from " + src.getName() + " to " + dest.getName());
        }
      }
    } else {
      synchronized (dest) {
        synchronized (src) {
          System.out.println("Contents Moved Successfully from " + src.getName() + " to " + dest.getName());
        }
      }
    }
  }
}
