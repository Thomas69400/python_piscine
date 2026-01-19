class Plant:
    """Define all information about a plant"""

    def __init__(self, name: str, height: int, age_days: int) -> None:
        """Create a plant and define its attributes attributes"""

        self.name = name
        self.height = height
        self.age_days = age_days
        self.growth = 0

    def grow(self) -> None:
        """Augment the height of the plant by 7 & set the growth param to 7"""

        self.height += 1
        self.growth += 1

    def age(self) -> None:
        """Augment the age of the plant by 7"""

        self.age_days += 1

    def get_info(self) -> None:
        """Display information about the plant"""

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
