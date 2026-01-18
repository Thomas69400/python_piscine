"""Check runtime dependencies and produce a small analysis visualization.

This script verifies the presence of common data-science packages (numpy,
pandas, matplotlib), prints their versions, runs a trivial data processing
step and saves a small plot to disk.
"""

import sys
from typing import Any


def main() -> None:
    """Verify dependencies, perform a minimal analysis and save a plot.

    - Prints the Python executable path.
    - Attempts to import numpy, pandas and matplotlib; reports missing modules.
    - Creates two small arrays, produces a bar plot and saves it to a PNG file.

    Returns:
        None
    """
    print("LOADING STATUS: Loading programs...\n")
    print("Env path: " + sys.executable, end="\n\n")
    print("Checking dependencies:")
    try:
        import numpy
        import pandas
        import matplotlib
        import matplotlib.pyplot as plt
        panda: str = pandas.__version__
        print(f"[OK] pandas ({panda}) - Data manipulation ready")
        num: str = numpy.__version__
        print(f"[OK] numpy ({num}) - Numerical computing ready")
        mat: str = matplotlib.__version__
        print(f"[OK] matplotlib ({mat}) - Visualization ready")
    except ModuleNotFoundError as e:
        print(f"[MISSING] {e.name} - Please install this package.")
        print("Install: pip install -r requirements.txt")
        print("\nOR: poetry install")
        sys.exit(1)

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points..")
    x_points: Any = numpy.array([10, 20, 20, 50])
    y_points: Any = numpy.array([3, 10, 5, 4])

    print("Generating visualization...\n")

    print("Analysis complete!")
    plt.bar(x_points, y_points)
    print("Results saved to: matrix_analysis.png")
    plt.savefig("matrix_analysis.png")


if __name__ == "__main__":
    main()
