"""Pydantic models and demo for validating alien contact reports.

This module defines ContactType and AlienContact models used to validate
incoming contact reports, and a small demonstration that constructs valid
and invalid examples to show validation behavior.
"""
from pydantic import (BaseModel, model_validator,
                      field_validator, ValidationError)
from datetime import datetime
from typing_extensions import Self
from typing import Optional, Dict, Any
from enum import Enum


class ContactType(Enum):
    """Enumeration of possible alien contact modalities."""
    RADIO: int = 1
    VISUAL: int = 2
    PHYSICAL: int = 3
    TELEPATHIC: int = 4


class AlienContact(BaseModel):
    """Model representing a recorded alien contact event.

    Attributes:
        contact_id: Unique contact identifier, must start with 'AC'
            and be 5-15 chars.
        timestamp: Datetime of the event.
        location: Human-readable location (3-100 chars).
        contact_type: ContactType instance describing modalities.
        signal_strength: Float in range 0.0-10.0.
        duration_minutes: Duration of contact in minutes (1-1440).
        witness_count: Number of witnesses (0-100).
        message_received: Optional textual message (<=500 chars).
        is_verified: Boolean flag marking verification status.
    """
    contact_id: str
    timestamp: datetime
    location: str
    contact_type: ContactType
    signal_strength: float
    duration_minutes: int
    witness_count: int
    message_received: Optional[str] = None
    is_verified: bool = False

    @field_validator('contact_id')
    def contact_id_is_valid(cls, contact_id: str) -> str:
        """Validate contact_id length.

        Raises ValueError if contact_id is not between 5 and 15 characters.
        """
        if not (5 <= len(contact_id) <= 15):
            raise ValueError(
                'contact_id must be between 5 and 15 characters long')
        return contact_id

    @field_validator('location')
    def location_is_valid(cls, location: str) -> str:
        """Validate location length.

        Raises ValueError if location is not between 3 and 100 characters.
        """
        if not (3 <= len(location) <= 100):
            raise ValueError(
                'location must be between 3 and 100 characters long')
        return location

    @field_validator('signal_strength')
    def signal_strength_is_valid(cls, signal_strength: float) -> float:
        """Validate signal_strength range (0.0-10.0)."""
        if not (0.0 <= signal_strength <= 10.0):
            raise ValueError('signal_strength must be between 0.0 and 10.0')
        return signal_strength

    @field_validator('duration_minutes')
    def duration_minutes_is_valid(cls, duration_minutes: int) -> int:
        """Validate duration_minutes range (1-1440)."""
        if not (1 <= duration_minutes <= 1440):
            raise ValueError('duration_minutes must be between 1 and 1440')
        return duration_minutes

    @field_validator('witness_count')
    def witness_count_is_valid(cls, witness_count: int) -> int:
        """Validate witness_count range (0-100)."""
        if not (1 <= witness_count <= 100):
            raise ValueError('witness_count must be between 0 and 100')
        return witness_count

    @field_validator('message_received')
    def message_received_is_valid(cls,
                                  message_received: Optional[str]) -> Optional[
                                      str]:
        """Validate optional message_received length (<=500 chars)."""
        if message_received is not None and len(message_received) > 500:
            raise ValueError(
                'message_received must be less than 500 characters long')
        return message_received

    @model_validator(mode='after')
    def validate_id(self) -> Self:
        """Ensure contact_id starts with 'AC'."""
        if not self.contact_id.startswith('AC'):
            raise ValueError('contact_id must start with "AC"')
        return self

    @model_validator(mode='after')
    def validate_telepathic(self) -> Self:
        """Ensure telepathic contact has at least three witnesses."""
        if (self.contact_type == ContactType.TELEPATHIC
                and self.witness_count < 3):
            raise ValueError(
                'telepathic contacts must have at least three witnesses')
        return self

    @model_validator(mode='after')
    def is_message_with_strong_signal(self) -> Self:
        """Ensure message_received is present if signal_strength > 7.0."""
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                'message_received must be provided for strong signals')
        return self

    @model_validator(mode='after')
    def validate_physical(self) -> Self:
        """Ensure physical contact reports are verified."""
        if (self.contact_type == ContactType.PHYSICAL
                and not self.is_verified):
            raise ValueError(
                'physical contact reports must be verified')
        return self

    def print_contact(self) -> None:
        """Print a summary of the alien contact."""
        print("======================================")
        # Note: keep original iteration logic to preserve behavior
        print("Valid contact report:")
        print(f"Contact ID: {self.contact_id}")
        print(f"Type: {self.contact_type.name}")
        print(f"Location: {self.location}")
        print(f"Signal: {self.signal_strength}/10")
        print(f"Duration: {self.duration_minutes} minutes")
        print(f"Witness: {self.witness_count}")
        print(f"Message: {self.message_received}")
        print("\n======================================")


def main() -> None:
    """Demo routine building valid and invalid AlienContact payloads and
    validating them."""
    print("Alien Contact Log Validation")

    alien_data: Dict[str, Any] = {
        "contact_id": "AC_1234_56",
        "timestamp": "2024-06-15T14:30:00Z",
        "location": "Sector 7G, Near Jupiter",
        "contact_type": ContactType.RADIO,
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": "We come in peace.",
        "is_verified": False
    }

    try:
        alien = AlienContact(**alien_data)
        alien.print_contact()
    except ValidationError as e:
        print("Validation Error:", e)

    invalid_alien_data: Dict[str, Any] = {
        "contact_id": "9999999",
        "timestamp": "2024-06-15T14:30:00Z",
        "location": "Area 51",
        "contact_type": ContactType.TELEPATHIC,
        "signal_strength": 8.0,
        "duration_minutes": 2,
        "witness_count": 4,
        "message_received": "None",
        "is_verified": False
    }

    try:
        print("Expected validation error:")
        invalid_alien = AlienContact(**invalid_alien_data)
        invalid_alien.print_contact()
    except ValidationError as e:
        print("Validation Error:", e)


if __name__ == "__main__":
    main()
