import java.util.ArrayList;
import java.util.List;

public class ClientManager {

    public static void main(String[] args) {

        FileProcess thread1 = new FileProcess("Thread 1 is writing");
        thread1.start();
        FileProcess thread2 = new FileProcess("Thread 2 is writing");
        thread2.start();
        FileProcess thread3 = new FileProcess("Thread 3 is writing");
        thread3.start();
        FileProcess thread4 = new FileProcess("Thread 4 is writing");
        thread4.start();

        try {
            thread1.join();
            thread2.join();
            thread3.join();
            thread4.join();
        } catch (InterruptedException e) {
            System.err.println("Hilo interrumpido: " + e.getMessage());
        }

        // -- Finaliza ejecución de hilos

        // Crear lista para el analizador
        List<FileProcess> procesos = new ArrayList<>();
        procesos.add(thread1);
        procesos.add(thread2);
        procesos.add(thread3);
        procesos.add(thread4);
        
        ResultAnalyzer analyzer = new ResultAnalyzer(procesos);
        analyzer.exportarCSV("logAnalisisSafeThread.csv");
    }
}

class FileProcess extends Thread {
    
    private String msgLog;
    private long tiempoObtenerLogger;
    private long tiempoEscritura;
    private int cantidadMensajes = 50;

    public FileProcess(String msg) {
        this.msgLog = msg;
    }

    @Override
    public void run() {
        // Medir tiempo para obtener el FileLogger
        long tiFL = System.nanoTime();
        Logger fileLogger = FileLogger.getFileLogger(); // Asumo que Logger y FileLogger existen
        tiempoObtenerLogger = System.nanoTime() - tiFL;

        // Medir tiempo para escribir 50 mensajes
        long tiLog = System.nanoTime();
        for (int i = 0; i < cantidadMensajes; i++) {
            fileLogger.log(msgLog);
        }
        tiempoEscritura = System.nanoTime() - tiLog;
    }

    public long getTiempoObtenerLogger() { return tiempoObtenerLogger; }
    public long getTiempoEscritura()     { return tiempoEscritura; }
}