"""Pydantic model and demo for validating space station telemetry data.

This module defines a SpaceStation model using pydantic for runtime data
validation and provides a small CLI demo that constructs valid and invalid
instances to show validation behavior.
"""
from typing import Optional, Dict, Any
from datetime import datetime
from pydantic import BaseModel, field_validator, ValidationError


class SpaceStation(BaseModel):
    """Data model representing a space station's operational telemetry.

    Attributes:
        station_id: Unique station identifier (3-10 characters).
        name: Human-readable station name (1-50 characters).
        crew_size: Number of crew members (1-20).
        power_level: Power percentage (0.0-100.0).
        oxygen_level: Oxygen percentage (0.0-100.0).
        last_maintenance: Timestamp of last maintenance.
        is_operational: Operational flag (defaults to True).
        notes: Optional free-text notes (max 200 chars).
    """
    station_id: str
    name: str
    crew_size: int
    power_level: float
    oxygen_level: float
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = None

    @field_validator('station_id')
    def station_id_is_valid(cls, station_id: str) -> str:
        """Validate station_id length.

        Raises ValueError if station_id is not between 3 and 10 characters.
        """
        if not (3 <= len(station_id) <= 10):
            raise ValueError(
                'station_id must be between 3 and 10 characters long')
        return station_id

    @field_validator('name')
    def name_is_valid(cls, name: str) -> str:
        """Validate name length.

        Raises ValueError if name is not between 1 and 50 characters.
        """
        if not (1 <= len(name) <= 50):
            raise ValueError('name must be between 1 and 50 characters long')
        return name

    @field_validator('crew_size')
    def crew_size_is_valid(cls, crew_size: int) -> int:
        """Validate crew_size range (1-20)."""
        if not (1 <= crew_size <= 20):
            raise ValueError('crew_size must be between 1 and 20')
        return crew_size

    @field_validator('power_level')
    def power_level_is_valid(cls, power_level: float) -> float:
        """Validate power_level range (0.0-100.0)."""
        if not (0.0 <= power_level <= 100.0):
            raise ValueError('power_level must be between 0.0 and 100.0')
        return power_level

    @field_validator('oxygen_level')
    def oxygen_level_is_valid(cls, oxygen_level: float) -> float:
        """Validate oxygen_level range (0.0-100.0)."""
        if not (0.0 <= oxygen_level <= 100.0):
            raise ValueError('oxygen_level must be between 0.0 and 100.0')
        return oxygen_level

    @field_validator('notes')
    def notes_is_valid(cls, notes: Optional[str]) -> Optional[str]:
        """Validate optional notes length (<=200 chars)."""
        if notes is not None and len(notes) > 200:
            raise ValueError('notes must be less than 200 characters long')
        return notes

    def print_station(self) -> None:
        """Print a human-readable summary of the station instance to stdout."""
        print("========================================")
        print("Valid station created:")
        print("ID:", self.station_id)
        print("Name:", self.name)
        print("Crew:", self.crew_size)
        print("Power:", self.power_level)
        print("Last Maintenance:", self.last_maintenance.isoformat())
        print("Oxygen:", self.oxygen_level)
        if self.is_operational:
            print("Status: Operational")
        else:
            print("Status: Non-operational")
        if self.notes:
            print("Notes:", self.notes)
        print("\n========================================")


def main() -> None:
    """Demonstration routine that creates valid and invalid
    SpaceStation instances.

    - Constructs a valid SpaceStation and prints it.
    - Attempts to construct an invalid instance to show
    pydantic validation errors.
    """
    print("Space Station Data Validation")
    print("========================================")
    try:
        valid_station: SpaceStation = SpaceStation(
            station_id="SS-001",
            name="Orbital One",
            crew_size=6,
            power_level=95.5,
            oxygen_level=98.0,
            last_maintenance=datetime(2024, 5, 20, 14, 30),
            is_operational=True,
            notes="All systems nominal."
        )
        valid_station.print_station()
    except ValidationError as e:
        print("Validation Error:", e)

    invalid_station_data: Dict[str, Any] = {
        "station_id": "SS001",
        "name": "ISS",
        "crew_size": 20,
        "power_level": 10.0,
        "oxygen_level": 5.0,
        "last_maintenance": True,
        "is_operational": True,
        "notes": None
    }
    try:
        print("Expected validation error:")
        invalid_station = SpaceStation(**invalid_station_data)
        invalid_station.print_station()
    except ValidationError as e:
        print("Validation Error:", e)


if __name__ == "__main__":
    main()
