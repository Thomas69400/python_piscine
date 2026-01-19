from pydantic import BaseModel, field_validator, \
    model_validator, ValidationError
from datetime import datetime
from typing import List, Type
from enum import Enum
from typing_extensions import Self

"""space_crew module

Provides Pydantic models for CrewMember and SpaceMission with validation.
"""


class Rank(Enum):
    """Enumeration of possible crew ranks, with increasing seniority values."""
    CADET: int = 1
    OFFICER: int = 2
    LIEUTENANT: int = 3
    CAPTAIN: int = 4
    COMMANDER: int = 5


class CrewMember(BaseModel):
    """Model representing a crew member.

    Attributes:
        member_id: Unique identifier for the crew member.
        name: Full name of the crew member.
        rank: Rank of the crew member (Rank enum).
        age: Age in years.
        specialization: Role or specialization on the mission.
        years_of_experience: Years of professional experience.
        is_active: Whether the crew member is active and eligible for missions.
    """
    member_id: str
    name: str
    rank: Rank
    age: int
    specialization: str
    years_of_experience: int
    is_active: bool = True

    @field_validator("member_id")
    def validate_member_id(cls: Type['CrewMember'], v: str) -> str:
        """Validate member_id length (3-10 characters)."""
        if not 3 <= len(v) <= 10:
            raise ValueError(
                "member_id must be between 3 and 10 characters long")
        return v

    @field_validator("name")
    def validate_name(cls: Type['CrewMember'], v: str) -> str:
        """Validate name length (2-50 characters)."""
        if not 2 <= len(v) <= 50:
            raise ValueError("name must be between 2 and 50 characters long")
        return v

    @field_validator("age")
    def validate_age(cls: Type['CrewMember'], v: int) -> int:
        """Validate age is between 18 and 80."""
        if not 18 <= v <= 80:
            raise ValueError("age must be between 18 and 80")
        return v

    @field_validator("specialization")
    def validate_specialization(cls: Type['CrewMember'], v: str) -> str:
        """Validate specialization length (3-30 characters)."""
        if not 3 <= len(v) <= 30:
            raise ValueError("specialization must be between 3 and 30 " +
                             "characters long")
        return v

    @field_validator("years_of_experience")
    def validate_years_of_experience(cls: Type['CrewMember'], v: int) -> int:
        """Validate years_of_experience is between 0 and 50."""
        if not 0 <= v <= 50:
            raise ValueError("years_of_experience must be between 0 and 50")
        return v


class SpaceMission(BaseModel):
    """Model representing a space mission with crew and mission constraints.

    Attributes:
        mission_id: Identifier for the mission (must start with 'M').
        mission_name: Human-readable name of the mission.
        destination: Destination of the mission (e.g., planet name).
        launch_date: Scheduled launch datetime.
        duration_days: Mission duration in days.
        crew: List of CrewMember instances.
        mission_status: Current status of the mission.
        budget_million: Budget in millions.
    """
    mission_id: str
    mission_name: str
    destination: str
    launch_date: datetime
    duration_days: int
    crew: List[CrewMember]
    mission_status: str = "Planned"
    budget_million: float

    @field_validator("mission_id")
    def validate_mission_id(cls: Type['SpaceMission'], v: str) -> str:
        """Validate mission_id length (5-15 characters)."""
        if not 5 <= len(v) <= 15:
            raise ValueError(
                "mission_id must be between 5 and 15 characters long")
        return v

    @field_validator("mission_name")
    def validate_mission_name(cls: Type['SpaceMission'], v: str) -> str:
        """Validate mission_name length (3-100 characters)."""
        if not 3 <= len(v) <= 100:
            raise ValueError(
                "mission_name must be between 3 and 100 characters long")
        return v

    @field_validator("destination")
    def validate_destination(cls: Type['SpaceMission'], v: str) -> str:
        """Validate destination length (3-50 characters)."""
        if not 3 <= len(v) <= 50:
            raise ValueError(
                "destination must be between 3 and 50 characters long")
        return v

    @field_validator("duration_days")
    def validate_duration_days(cls: Type['SpaceMission'], v: int) -> int:
        """Validate duration_days is between 1 and 3650."""
        if not 1 <= v <= 3650:
            raise ValueError("duration_days must be between 1 and 3650")
        return v

    @field_validator("crew")
    def validate_crew(cls: Type['SpaceMission'],
                      v: List[CrewMember]) -> List[CrewMember]:
        """Validate crew size is between 1 and 12 members."""
        if not 1 <= len(v) <= 12:
            raise ValueError("crew must have at least one CrewMember and " +
                             "less than or equal to 12 CrewMembers")
        return v

    @field_validator("budget_million")
    def validate_budget_million(cls: Type['SpaceMission'], v: float) -> float:
        """Validate budget_million is between 1 and 10000."""
        if not 1 <= v <= 10000:
            raise ValueError("budget_million must be between 1 and 10000")
        return v

    @model_validator(mode="after")
    def mission_id_starts_with_m(self) -> Self:
        """Ensure mission_id starts with 'M'."""
        if not self.mission_id.startswith("M"):
            raise ValueError("mission_id must start with 'M'")
        return self

    @model_validator(mode="after")
    def mission_has_commander_or_captain(self) -> Self:
        """Ensure mission has at least one Commander or Captain in the crew."""
        if not any(
            member.rank in {Rank.COMMANDER, Rank.CAPTAIN}
            for member in self.crew
        ):
            raise ValueError("mission must have at least one Commander or " +
                             "Captain in the crew")
        return self

    @model_validator(mode="after")
    def long_mission(self) -> Self:
        """For missions longer than 365 days, require >=50% members with 5+
        years experience."""
        if self.duration_days > 365:
            experienced_members = [
                member for member in self.crew
                if member.years_of_experience >= 5
            ]
            if len(experienced_members)/len(self.crew) < 0.5:
                raise ValueError("Long missions (>365 days) must have at " +
                                 "least 50% crew members with 5+ years of " +
                                 "experience")
        return self

    @model_validator(mode="after")
    def all_active(self) -> Self:
        """Ensure all crew members are active for the mission."""
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self

    def print_mission_summary(self) -> None:
        """Print a human-readable summary of the mission to stdout."""
        print("=========================================")
        print("Valid mission created:")
        print(f"Mission '{self.mission_name}'")
        print(f"ID: {self.mission_id}")
        print(f"Destination: {self.destination}")
        print(f"Duration: {self.duration_days} days")
        print(f"Budget: ${self.budget_million}M")
        print(f"Crew size: {len(self.crew)}")
        print("Crew Members:")
        for member in self.crew:
            print(f" - {member.name} - {member.specialization}")
        print("\n=========================================")


def main() -> None:
    """Entry point for manual execution: construct sample missions and show
    validation."""
    print("Space Mission Crew Validation")

    try:
        crew: List[CrewMember] = [
            CrewMember(
                member_id="CM001",
                name="Alice Smith",
                rank=Rank.CAPTAIN,
                age=35,
                specialization="Pilot",
                years_of_experience=10,
            ),
            CrewMember(
                member_id="CM002",
                name="Bob Johnson",
                rank=Rank.LIEUTENANT,
                age=29,
                specialization="Engineer",
                years_of_experience=6,
            ),
            CrewMember(
                member_id="CM003",
                name="Charlie Lee",
                rank=Rank.OFFICER,
                age=32,
                specialization="Scientist",
                years_of_experience=4,
            ),
        ]

        mission: SpaceMission = SpaceMission(
            mission_id="M12345",
            mission_name="Mars Exploration",
            destination="Mars",
            launch_date=datetime(2030, 5, 14),
            duration_days=400,
            crew=crew,
            budget_million=5000,
        )

        mission.print_mission_summary()
    except ValidationError as e:
        print("Validation Error:")
        print(e)

    try:
        print("Expected validation error:")
        invalid_crew: List[CrewMember] = [
            CrewMember(
                member_id="CM004",
                name="Dave Brown",
                rank=Rank.CAPTAIN,
                age=28,
                specialization="Medic",
                years_of_experience=2,
                is_active=True,
            ),
        ]

        invalid_mission: SpaceMission = SpaceMission(
            mission_id="x99999",
            mission_name="Venus Flyby",
            destination="Venus",
            launch_date=datetime(2029, 8, 20),
            duration_days=30,
            crew=invalid_crew,
            budget_million=2000.0,
        )

        invalid_mission.print_mission_summary()
    except ValidationError as e:
        print("Validation Error for invalid mission:")
        print(e)


if __name__ == "__main__":
    main()
