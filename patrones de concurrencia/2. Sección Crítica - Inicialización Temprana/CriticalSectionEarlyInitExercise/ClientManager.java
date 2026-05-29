
public class ClientManager {

	private static final int NUM_THREADS = 4;

    public static void main(String[] args) {

        FileProcess[] procesos = new FileProcess[NUM_THREADS];
        for (int i = 0; i < NUM_THREADS; i++) {
            procesos[i] = new FileProcess("Thread " + (i + 1) + " is writting");
            procesos[i].start();
        }

        for (FileProcess proceso : procesos) {
            try {
                proceso.join();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                System.err.println("Hilo interrumpido: " + e.getMessage());
            }
        }

		// -- Finaliza ejecución de hilos

        ResultAnalyzer analyzer = new ResultAnalyzer(procesos);
        analyzer.exportarCSV("logAnalisisEarlyInit.csv");
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
        Logger fileLogger = FileLogger.getFileLogger();
        tiempoObtenerLogger = System.nanoTime() - tiFL;

        // Medir tiempo para escribir 100 mensajes
        long tiLog = System.nanoTime();
        for (int i = 0; i < cantidadMensajes; i++) {
            fileLogger.log(msgLog);
        }
        tiempoEscritura = System.nanoTime() - tiLog;
    }

    public long getTiempoObtenerLogger() { return tiempoObtenerLogger; }
    public long getTiempoEscritura()     { return tiempoEscritura; }
}