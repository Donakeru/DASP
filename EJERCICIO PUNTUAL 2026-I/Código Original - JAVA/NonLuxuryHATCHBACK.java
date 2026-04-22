public class NonLuxuryHATCHBACK implements NonLuxury {
    private String name;

    public NonLuxuryHATCHBACK(String sName) {
        name = sName;
    }

    public String getNLName() {
        return name;
    }

    public String getNLFeatures() {
        return "Non-Luxury HATCHBACK Features ";
    };
}
