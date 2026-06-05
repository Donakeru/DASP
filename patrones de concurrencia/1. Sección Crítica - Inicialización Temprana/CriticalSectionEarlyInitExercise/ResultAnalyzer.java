import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;

public class ResultAnalyzer {

    private final List<FileProcess> procesos;

    public ResultAnalyzer(List<FileProcess> procesos) {
        this.procesos = procesos;
    }

    public void exportarCSV(String rutaArchivo) {
        try {
            File archivo = new File(rutaArchivo);
            boolean archivoNuevo = !archivo.exists() || archivo.length() == 0;

            try (PrintWriter pw = new PrintWriter(new FileWriter(rutaArchivo, true))) {
                // Solo escribir headers si el archivo es nuevo
                if (archivoNuevo) {
                    pw.println("Hilo,TiempoObtenerLogger(ns),TiempoEscritura50Mensajes(ns)");
                }

                int contador = 1;
                for (FileProcess proceso : procesos) {
                    pw.println("Thread " + contador++
                            + "," + proceso.getTiempoObtenerLogger()
                            + "," + proceso.getTiempoEscritura());
                }
                System.out.println("Análisis exportado a: " + rutaArchivo);
            }
        } catch (IOException e) {
            System.err.println("Error exportando CSV: " + e.getMessage());
        }
    }
}