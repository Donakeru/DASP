import java.util.*;
import java.io.*;

public class LoggerFactory {

  public int isFileLoggingEnabled() {
    Properties p = new Properties();
    try {
      p.load(ClassLoader.getSystemResourceAsStream(
        "Output.type"));
      String fileLoggingValue = p.getProperty("Output");
      System.out.println("Writing to " + fileLoggingValue);
      if (fileLoggingValue.equalsIgnoreCase("FILE"))
      {return 1;}
      else if (fileLoggingValue.equalsIgnoreCase("CONSOLE"))
      {return 2;}
      else 
      {System.out.println("The output type was not defined or not recognized.Using the default output: Console"); 
      return 2;}
    }
    catch (IOException e) {
    	System.out.println("The output type was not available.Using the default output: Console");
    	return 2;
    }
  }
  
  public Logger getLogger() {
    if (isFileLoggingEnabled() == 1) 
      return new FileLogger();
    else 
      return new ConsoleLogger();
  }
}

