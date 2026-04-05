/**
 * 
 * ENFOQUE DE DISEÑO I
 * Se define una interfaz FlyweightIntr a ser implementada por la clase
 * Flyweight que representa los datos intrínsecos de la tarjeta de visita:
 * 
 */

public interface FlyweightIntr {
  public String getNameFac();

  public String getLocality();

  public String getAddress();

  public String getNeighbourhood();

  public String getCoordinates();

  /**
   * 
   * ENFOQUE DE DISEÑO II
   * 
   * En este enfoque, los datos extrínsecos se pasan al objeto Flyweight como
   * parte de una llamada a un método, en lugar de ser representados como un
   * objeto separado.
   * 
   * @param name
   * @param code
   */
  public void print(String name, String code);
}
