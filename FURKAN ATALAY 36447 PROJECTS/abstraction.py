# --- ABSTRACTION EXAMPLE ---
from abc import ABC, abstractmethod

# Abstract Parent Class (A blueprint, cannot create objects directly from this)
class RemoteControl(ABC):
    @abstractmethod
    def press_power_button(self):
        pass

# Concrete Child Class implementing the abstract method
class TVRemote(RemoteControl):
    def press_power_button(self):
        # The user just presses the button, internal technical details are hidden
        print("TV screen is turning on...")

# --- TESTING ABSTRACTION ---
if __name__ == "__main__":
    # my_remote = RemoteControl() # ERROR: Cannot instantiate abstract class
    remote = TVRemote()
    remote.press_power_button() # Output: TV screen is turning on...