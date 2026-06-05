public class FileSysManager{

  public static void main(String[] args){

    Directory dir1 = new Directory("Directory_1");
    Directory dir2 = new Directory("Directory_2");

    FileSysUtil_Rev fileSysUtil = new FileSysUtil_Rev();

    FileSysProcess proceso1 = new FileSysProcess(dir1, dir2, fileSysUtil);
    proceso1.start();
    
    FileSysProcess proceso2 = new FileSysProcess(dir2, dir1, fileSysUtil);
    proceso2.start();
  }
}

class FileSysProcess extends Thread{

  private Directory dir1;
  private Directory dir2;
  private FileSysUtil_Rev fileSysUtil;

  public FileSysProcess(Directory src, Directory dest, FileSysUtil_Rev fileSysUtil){
    this.dir1 = src;
    this.dir2 = dest;
    this.fileSysUtil = fileSysUtil;
  }

  @Override
  public void run(){
    fileSysUtil.moveContents(dir1, dir2);
  }

}
