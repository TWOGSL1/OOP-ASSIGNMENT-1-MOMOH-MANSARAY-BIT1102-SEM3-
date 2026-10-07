"""Open-field crop yield monitor: an OOP and privacy-first teaching example."""


class CropPlot:
    """A field record identified by a non-personal plot code."""

    DEFAULT_CROP = "Maize"
    records_created = 0

    def __init__(self, plot_id, crop, area_hectares, yield_tonnes=0.0):
        self.plot_id = plot_id.strip().upper()
        self.crop = crop.strip().title()
        self.area_hectares = float(area_hectares)
        self.yield_tonnes = float(yield_tonnes)
        self.validate_measurements(self.area_hectares, self.yield_tonnes)
        CropPlot.records_created += 1

    @classmethod
    def from_default_crop(cls, plot_id, area_hectares, yield_tonnes=0.0):
        """Create a plot using the class-wide default crop."""
        return cls(plot_id, cls.DEFAULT_CROP, area_hectares, yield_tonnes)

    @staticmethod
    def validate_measurements(area_hectares, yield_tonnes):
        """Reject impossible negative/non-numeric field measurements."""
        if area_hectares <= 0:
            raise ValueError("Area must be greater than zero hectares.")
        if yield_tonnes < 0:
            raise ValueError("Yield cannot be negative.")

    def update_yield(self, yield_tonnes):
        """Instance method: update this plot's measured yield."""
        yield_tonnes = float(yield_tonnes)
        self.validate_measurements(self.area_hectares, yield_tonnes)
        self.yield_tonnes = yield_tonnes

    def yield_per_hectare(self):
        return self.yield_tonnes / self.area_hectares

    def display_info(self):
        return (
            f"{self.plot_id} | {self.crop} | {self.area_hectares:.2f} ha | "
            f"{self.yield_tonnes:.2f} tonnes | "
            f"{self.yield_per_hectare():.2f} tonnes/ha"
        )


class FarmRegistry:
    """Stores multiple CropPlot objects in one dictionary keyed by plot ID."""

    def __init__(self):
        self.plots = {}

    def add_plot(self, plot):
        if plot.plot_id in self.plots:
            raise ValueError("That plot ID already exists.")
        self.plots[plot.plot_id] = plot

    def display_records(self):
        if not self.plots:
            print("No plot records have been added yet.")
            return
        print("\nPLOT | CROP | AREA | TOTAL YIELD | YIELD PER HECTARE")
        print("-" * 66)
        for plot in self.plots.values():
            print(plot.display_info())

    def update_plot_yield(self, plot_id, yield_tonnes):
        plot_id = plot_id.strip().upper()
        if plot_id not in self.plots:
            raise KeyError("Plot ID was not found.")
        self.plots[plot_id].update_yield(yield_tonnes)


def read_positive_number(prompt, allow_zero=False):
    while True:

        try:
            value = float(input(prompt))
            if value < 0 or (value == 0 and not allow_zero):
                print("Enter a valid positive number.")
                continue
            return value
        except ValueError:
            print("Enter a number, such as 2.5.")


def add_plot(registry):
    plot_id = input("Non-personal plot ID (for example F-001): ").strip()
    crop = input("Crop name: ").strip() or CropPlot.DEFAULT_CROP
    area = read_positive_number("Area in hectares: ")
    yield_amount = read_positive_number("Yield in tonnes (0 if not measured): ", True)
    try:
        registry.add_plot(CropPlot(plot_id, crop, area, yield_amount))
        print("Plot record added.")
    except ValueError as error:
        print(f"Could not add record: {error}")


def update_yield(registry):
    plot_id = input("Plot ID to update: ")
    amount = read_positive_number("New yield in tonnes: ", True)
    try:
        registry.update_plot_yield(plot_id, amount)
        print("Yield updated.")
    except (ValueError, KeyError) as error:
        print(f"Could not update record: {error}")


def main():
    registry = FarmRegistry()
    while True:
        print("\nOPEN-FIELD CROP YIELD MONITOR")
        print("1. Add plot  2. Display plots  3. Update yield  4. Exit")
        choice = input("Choose 1-4: ").strip()
        if choice == "1":
            add_plot(registry)
        elif choice == "2":
            registry.display_records()
        elif choice == "3":
            update_yield(registry)
        elif choice == "4":
            print("Thank you. Plot data remains in memory for this session only.")
            break
        else:
            print("Choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
