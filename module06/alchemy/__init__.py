"""Top-level alchemy package: expose selected elemental helpers and metadata.
"""

from .elements import create_fire, create_water

__version__: str = "1.0.0"
__author__: str = "Master Pythonicus"

__all__: list[str] = ["create_fire",
                      "create_water", "__version__", "__author__"]
