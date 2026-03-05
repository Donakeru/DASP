public abstract class VehicleFactory {
  public static final String CAR = "Car";
  public static final String SUV = "Suv";


  public abstract Luxury getLuxury();
  public abstract NonLuxury getNonLuxury();

  public static VehicleFactory getVehicleFactory(String type) {
    if (type.equals(VehicleFactory.CAR))
      return new CARVehicleFactory();
    if (type.equals(VehicleFactory.SUV))
      return new SUVVehicleFactory();

    return new CARVehicleFactory();
  }

} // End of class


