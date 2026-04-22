public class HATCHBACKVehicleFactory extends VehicleFactory {

  public LuxuryHATCHBACK getLuxury() {
    return new LuxuryHATCHBACK("Hatchback-Luxury");
  }
  public NonLuxuryHATCHBACK getNonLuxury() {
    return new NonLuxuryHATCHBACK("Hatchback-NonLuxury");
  }
} // End of class


