"""
Abstract Factory Pattern - Vehicle Search Application
A Python translation of the Java AutoSearchUI application using tkinter.
"""

import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod
from typing import Optional


# ==================== Abstract Factory ====================

class VehicleFactory(ABC):
    """Abstract factory for creating vehicle objects."""
    
    CAR = "Car"
    SUV = "Suv"
    HATCHBACK = "Hatchback"
    
    @abstractmethod
    def get_luxury(self) -> 'Luxury':
        """Create a luxury vehicle."""
        pass
    
    @abstractmethod
    def get_non_luxury(self) -> 'NonLuxury':
        """Create a non-luxury vehicle."""
        pass
    
    @staticmethod
    def get_vehicle_factory(vehicle_type: str) -> 'VehicleFactory':
        """Factory method to get the appropriate concrete factory."""
        if vehicle_type == VehicleFactory.CAR:
            return CARVehicleFactory()
        elif vehicle_type == VehicleFactory.SUV:
            return SUVVehicleFactory()
        elif vehicle_type == VehicleFactory.HATCHBACK:
            return HATCHBACKVehicleFactory()
        return CARVehicleFactory()  # Default


# ==================== Concrete Factories ====================

class CARVehicleFactory(VehicleFactory):
    """Concrete factory for CAR vehicles."""
    
    def get_luxury(self) -> 'LuxuryCAR':
        return LuxuryCAR("Luxury-Car")
    
    def get_non_luxury(self) -> 'NonLuxuryCAR':
        return NonLuxuryCAR("NonLuxury-Car")


class SUVVehicleFactory(VehicleFactory):
    """Concrete factory for SUV vehicles."""
    
    def get_luxury(self) -> 'LuxurySUV':
        return LuxurySUV("Luxury-SUV")
    
    def get_non_luxury(self) -> 'NonLuxurySUV':
        return NonLuxurySUV("Non-Luxury-SUV")


class HATCHBACKVehicleFactory(VehicleFactory):
    """Concrete factory for HATCHBACK vehicles."""
    
    def get_luxury(self) -> 'LuxuryHATCHBACK':
        return LuxuryHATCHBACK("Hatchback-Luxury")
    
    def get_non_luxury(self) -> 'NonLuxuryHATCHBACK':
        return NonLuxuryHATCHBACK("Hatchback-NonLuxury")


# ==================== Product Interfaces (Abstract Base Classes) ====================

class Luxury(ABC):
    """Interface for luxury vehicles."""
    
    @abstractmethod
    def get_luxury_name(self) -> str:
        pass
    
    @abstractmethod
    def get_luxury_features(self) -> str:
        pass


class NonLuxury(ABC):
    """Interface for non-luxury vehicles."""
    
    @abstractmethod
    def get_nl_name(self) -> str:
        pass
    
    @abstractmethod
    def get_nl_features(self) -> str:
        pass


# ==================== Concrete Luxury Products ====================

class LuxuryCAR(Luxury):
    """Concrete luxury CAR product."""
    
    def __init__(self, name: str):
        self._name = name
    
    def get_luxury_name(self) -> str:
        return self._name
    
    def get_luxury_features(self) -> str:
        return "Luxury Car Features"


class LuxurySUV(Luxury):
    """Concrete luxury SUV product."""
    
    def __init__(self, name: str):
        self._name = name
    
    def get_luxury_name(self) -> str:
        return self._name
    
    def get_luxury_features(self) -> str:
        return "Luxury SUV Features"


class LuxuryHATCHBACK(Luxury):
    """Concrete luxury HATCHBACK product."""
    
    def __init__(self, name: str):
        self._name = name
    
    def get_luxury_name(self) -> str:
        return self._name
    
    def get_luxury_features(self) -> str:
        return "Luxury HATCHBACK Features"


# ==================== Concrete Non-Luxury Products ====================

class NonLuxuryCAR(NonLuxury):
    """Concrete non-luxury CAR product."""
    
    def __init__(self, name: str):
        self._name = name
    
    def get_nl_name(self) -> str:
        return self._name
    
    def get_nl_features(self) -> str:
        return "Non-Luxury CAR Features"


class NonLuxurySUV(NonLuxury):
    """Concrete non-luxury SUV product."""
    
    def __init__(self, name: str):
        self._name = name
    
    def get_nl_name(self) -> str:
        return self._name
    
    def get_nl_features(self) -> str:
        return "Non-Luxury SUV Features"


class NonLuxuryHATCHBACK(NonLuxury):
    """Concrete non-luxury HATCHBACK product."""
    
    def __init__(self, name: str):
        self._name = name
    
    def get_nl_name(self) -> str:
        return self._name
    
    def get_nl_features(self) -> str:
        return "Non-Luxury HATCHBACK Features"


# ==================== Main GUI Application ====================

class AutoSearchUI:
    """Main GUI application using tkinter."""
    
    LUXURY = "Luxury"
    NON_LUXURY = "Non-Luxury"
    SEARCH = "Search"
    EXIT = "Exit"
    
    def __init__(self):
        self._root = tk.Tk()
        self._root.title("Abstract Factory - Example")
        self._root.geometry("1050x600")
        
        # Handle window close event
        self._root.protocol("WM_DELETE_WINDOW", self._on_exit)
        
        # Create GUI components
        self._create_widgets()
        self._layout_widgets()
        
    def _create_widgets(self):
        """Create all GUI widgets."""
        # Category combobox
        self._cmb_vehicle_category = ttk.Combobox(
            self._root, 
            values=[self.LUXURY, self.NON_LUXURY],
            state="readonly"
        )
        self._cmb_vehicle_category.set(self.LUXURY)
        
        # Vehicle type combobox
        self._cmb_vehicle_type = ttk.Combobox(
            self._root,
            values=[VehicleFactory.CAR, VehicleFactory.SUV, VehicleFactory.HATCHBACK],
            state="readonly"
        )
        self._cmb_vehicle_type.set(VehicleFactory.CAR)
        
        # Labels
        self._lbl_vehicle_category = ttk.Label(self._root, text="Vehicle Category:")
        self._lbl_vehicle_type = ttk.Label(self._root, text="Vehicle Type:")
        self._lbl_car_name = ttk.Label(self._root, text="Search Result:")
        self._lbl_car_name_value = ttk.Label(
            self._root, 
            text=" Please click on Search button"
        )
        
        # Buttons
        self._btn_search = ttk.Button(
            self._root, 
            text=self.SEARCH, 
            command=self._on_search
        )
        self._btn_exit = ttk.Button(
            self._root, 
            text=self.EXIT, 
            command=self._on_exit
        )
        
    def _layout_widgets(self):
        """Layout widgets using grid geometry manager."""
        # Configure grid padding
        pad_options = {'padx': 5, 'pady': 5}
        
        # Row 0: Vehicle Category
        self._lbl_vehicle_category.grid(row=0, column=0, sticky='e', **pad_options)
        self._cmb_vehicle_category.grid(row=0, column=1, sticky='w', **pad_options)
        
        # Row 1: Vehicle Type
        self._lbl_vehicle_type.grid(row=1, column=0, sticky='e', **pad_options)
        self._cmb_vehicle_type.grid(row=1, column=1, sticky='w', **pad_options)
        
        # Row 2: Search Result label
        self._lbl_car_name.grid(row=2, column=0, sticky='e', **pad_options)
        self._lbl_car_name_value.grid(row=2, column=1, sticky='w', **pad_options)
        
        # Row 3: Buttons (with extra top padding)
        button_pad = {'padx': 2, 'pady': (40, 5)}
        self._btn_search.grid(row=3, column=0, sticky='e', **button_pad)
        self._btn_exit.grid(row=3, column=1, sticky='w', **button_pad)
        
        # Configure column weights for proper resizing
        self._root.columnconfigure(0, weight=1)
        self._root.columnconfigure(1, weight=1)
        
    def get_selected_category(self) -> str:
        """Get the selected vehicle category."""
        return self._cmb_vehicle_category.get()
    
    def get_selected_type(self) -> str:
        """Get the selected vehicle type."""
        return self._cmb_vehicle_type.get()
    
    def set_result(self, search_result: str):
        """Update the search result label."""
        self._lbl_car_name_value.config(text=search_result)
    
    def _on_search(self):
        """Handle search button click."""
        vh_category = self.get_selected_category()
        vh_type = self.get_selected_type()
        
        # Get the appropriate vehicle factory
        vf = VehicleFactory.get_vehicle_factory(vh_type)
        
        if vh_category == self.LUXURY:
            luxury_vehicle = vf.get_luxury()
            search_result = (f"Name: {luxury_vehicle.get_luxury_name()}  "
                           f"Features: {luxury_vehicle.get_luxury_features()}")
        else:  # NON_LUXURY
            non_luxury_vehicle = vf.get_non_luxury()
            search_result = (f"Name: {non_luxury_vehicle.get_nl_name()}  "
                           f"Features: {non_luxury_vehicle.get_nl_features()}")
        
        self.set_result(search_result)
    
    def _on_exit(self):
        """Handle exit button click or window close."""
        self._root.quit()
        self._root.destroy()
    
    def run(self):
        """Start the GUI application."""
        self._root.mainloop()


# ==================== Main Entry Point ====================

def main():
    """Main entry point of the application."""
    app = AutoSearchUI()
    app.run()


if __name__ == "__main__":
    main()