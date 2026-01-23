class Plant:
    """A plant tracking height (cm), age (days) and weekly growth."""

    def __init__(self, name: str, height: int, age_days: int) -> None:
        """Initialize Plant attributes."""

        self.name: str = name
        self.height: int = height
        self.age_days: int = age_days
        self.growth: int = 0

    def grow(self) -> None:
        """Increase height by 1 cm and track growth by 1 cm."""

        self.height += 1
        self.growth += 1

    def age(self) -> None:
        """Increase age by 1 day."""

        self.age_days += 1

    def get_info(self) -> None:
        """Print information about the plant"""

        print(f"{self.name} : {self.height} cm, {self.age_days} days old")


if __name__ == "__main__":
    """Create a plant then make it grow and age"""

    plants = [Plant("Rose", 25, 30), Plant("Tulip", 20, 20)]
    print("=== Day 1 ===")
    for p in plants:
        p.get_info()
        for i in range(1, 7):
            p.grow()
            p.age()
    print("=== Day 7 ===")
    for p in plants:
        p.get_info()
        print(f"Growth this week: +{p.growth}cm")
