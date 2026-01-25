from abc import ABC, abstractmethod
from typing import Any, Optional, List, Dict


class DataProcessor(ABC):
    """Abstract base class for data processors.

    Subclasses must implement process and validate to handle and check data.
    """

    def __init__(self) -> None:
        """Initialize DataProcessor."""
        super().__init__()

    @abstractmethod
    def process(self, data: Any) -> str:
        """Abstract method to process data

        Args:
            data (Any): the data to process

        Returns:
            str: the data processed
        """

        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Check if data is valid

        Args:
            data (Any): the data to validate

        Returns:
            bool: true if data is valid false either
        """

        pass

    def format_output(self, result: str) -> str:
        """Format a string

        Args:
            result (str): the base message to output

        Returns:
            str: the final output
        """

        return f"{result}"


class NumericProcessor(DataProcessor):
    """Processor for numeric data.

    Attributes:
        count: Number of numeric values processed.
        total: Sum of all numeric values.
        avg: Average of all numeric values.
    """

    def __init__(self) -> None:
        """Initialize NumericProcessor with accumulator attributes."""
        super().__init__()
        self.count: Optional[int] = None
        self.total: Optional[int] = None
        self.avg: Optional[float] = None

    def process(self, data: Any) -> str:
        """Process data

        Args:
            data (Any): the data to process

        Raises:
            ValueError: if data is not a int or list of int

        Returns:
            str: the data processed
        """

        if not self.validate(data):
            raise ValueError("Invalid data for NumericProcessor")
        self.count = len(data)
        self.total = sum(data)
        self.avg = self.total/self.count
        return f"Processing data: {data}"

    def validate(self, data: Any) -> bool:
        """Check if data if a int or list of int

        Args:
            data (Any): data to validate

        Returns:
            bool: true if int or list of int false either
        """

        if isinstance(data, int):
            return True
        if isinstance(data, list) and all(isinstance(x, int) for x in data):
            return True
        return False

    def format_output(self, result: str) -> str:
        """Format a string

        Args:
            result (str): the base message to output

        Returns:
            str: the final output
        """

        return result + \
            f"Processed {self.count} numeric values, " + \
            f"sum={self.total}, avg={self.avg}"


class TextProcessor(DataProcessor):
    """Processor for text data.

    Attributes:
        length: Length of the processed text.
        words: Number of words in the processed text.
    """

    def __init__(self) -> None:
        """Initialize TextProcessor with summary attributes."""
        super().__init__()
        self.length: Optional[int] = None
        self.words: Optional[int] = None

    def process(self, data: Any) -> str:
        """Process data

        Args:
            data (Any): the data to process

        Raises:
            ValueError: if data is not a str

        Returns:
            str: the data processed
        """

        if not self.validate(data):
            raise ValueError("Invalid data for TextProcessor")
        self.length = len(data)
        self.words = len(data.split())
        return f"Processing data: \"{data}\""

    def validate(self, data: Any) -> bool:
        """Check if data if a str

        Args:
            data (Any): data to validate

        Returns:
            bool: true if str false either
        """

        return isinstance(data, str)

    def format_output(self, result: str) -> str:
        """Format a string

        Args:
            result (str): the base message to output

        Returns:
            str: the final output
        """

        return result + \
            f"Processed text: {self.length} characters, {self.words} words"


class LogProcessor(DataProcessor):
    """Processor for log-entry dictionaries.

    Attributes:
        l_type: The log level type (e.g., ERROR, INFO).
        msg: The log message content.
    """

    def __init__(self) -> None:
        """Initialize LogProcessor with extracted log fields."""
        super().__init__()
        self.l_type: Optional[str] = None
        self.msg: Optional[str] = None

    def process(self, data: Any) -> str:
        """Process data

        Args:
            data (Any): the data to process

        Raises:
            ValueError: if data is not a dict

        Returns:
            str: the data processed
        """

        if not self.validate(data):
            raise ValueError("Invalid data for LogProcessor")
        for key in data:
            self.l_type = key
            self.msg = data[key]
        return f"Processing data: {data}"

    def validate(self, data: Any) -> bool:
        """Check if data if a dict

        Args:
            data (Any): data to validate

        Returns:
            bool: true if dict false either
        """

        return isinstance(data, dict)

    def format_output(self, result: str) -> str:
        """Format a string

        Args:
            result (str): the base message to output

        Returns:
            str: the final output
        """

        if self.l_type == "ERROR":
            return result + f"[ALERT] ERROR level detected: {self.msg}"
        elif self.l_type == "INFO":
            return result + f"[INFO] INFO level detected: {self.msg}"
        return result + f"[LOG] INFO level detected: {self.msg}"


def main() -> None:
    """Execute program.

    Demonstrates the usage of different data processors including
    NumericProcessor, TextProcessor, and LogProcessor through a
    unified interface.
    """
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    nume: NumericProcessor = NumericProcessor()
    lst: List[int] = [1, 2, 3, 4, 5]
    try:
        print(nume.process(lst))
        print("Validation: Numeric data verified")
        print(nume.format_output("Output: "), end="\n\n")
    except Exception as e:
        print(e, end="\n\n")

    print("Initializing Text Processor...")
    txt: TextProcessor = TextProcessor()
    s: str = "Hello Nexus World"
    try:
        print(txt.process(s))
        print("Validation: Text data verified")
        print(txt.format_output("Output: "), end="\n\n")
    except Exception as e:
        print(e, end="\n\n")

    print("Initializing Log Processor...")
    logs: LogProcessor = LogProcessor()
    dct: Dict[str, str] = {"ERROR": "Connection timeout"}
    try:
        print(logs.process(dct))
        print("Validation: Log entry verified")
        print(logs.format_output("Output: "), end="\n")
    except Exception as e:
        print(e, end="\n\n")

    print("\n=== Polymorphic Processing Demo ===")
    proc: Dict[DataProcessor, Any] = {
        NumericProcessor(): [1, 2, 3],
        TextProcessor(): "Hello World",
        LogProcessor(): {"INFO": "System ready"}
    }
    print("Processing multiple data types through same interface...")
    for i, p in enumerate(proc):
        try:
            p.process(proc[p])
            print(p.format_output(f"Result {i+1}: "), end="\n")
        except Exception as e:
            print(f"Error in processing: {e}")
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
