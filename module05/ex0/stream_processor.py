from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"{result}"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.count = None
        self.total = None
        self.avg = None

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for NumericProcessor")
        self.count = len(data)
        self.total = sum(data)
        self.avg = self.total/self.count
        return f"Processing data: {data}"

    def validate(self, data: Any) -> bool:
        try:
            assert isinstance(data, int) or (
                isinstance(data, list) and all(isinstance(x, int)
                                               for x in data)
            )
            return True
        except AssertionError:
            print("Error: Data must be an int or a list of ints")
        return False

    def format_output(self, result: str) -> str:
        return result + \
            f"Processed {self.count} numeric values, " + \
            f"sum={self.total}, avg={self.avg}"


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.length = None
        self.words = None

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for TextProcessor")
        self.length = len(data)
        self.words = len(data.split())
        return f"Processing data: \"{data}\""

    def validate(self, data: Any) -> bool:
        try:
            assert isinstance(data, str)
            return True
        except AssertionError:
            print("Error: Data must be a string.")
        return False

    def format_output(self, result: str) -> str:
        return result + \
            f"Processed text: {self.length} characters, {self.words} words"


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.l_type = None
        self.msg = None

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for LogProcessor")
        for key in data:
            self.l_type = key
            self.msg = data[key]
        return f"Processing data: {data}"

    def validate(self, data: Any) -> bool:
        try:
            assert isinstance(data, dict)
            return True
        except AssertionError as e:
            print(f"Error: {e}")
        return False

    def format_output(self, result: str) -> str:
        if self.l_type == "ERROR":
            return result + f"[ALERT] ERROR level detected: {self.msg}"
        elif self.l_type == "INFO":
            return result + f"[INFO] INFO level detected: {self.msg}"
        return result + f"[LOG] INFO level detected: {self.msg}"


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    nume = NumericProcessor()
    lst = [1, 2, 3, 4, 5, "test"]
    try:
        print(nume.process(lst))
        print("Validation: Numeric data verified")
        print(nume.format_output("Output: "), end="\n\n")
    except Exception as e:
        print(e, end="\n\n")

    print("Initializing Text Processor...")
    txt = TextProcessor()
    s = "Hello Nexus World"
    try:
        print(txt.process(s))
        print("Validation: Text data verified")
        print(txt.format_output("Output: "), end="\n\n")
    except Exception as e:
        print(e, end="\n\n")

    print("Initializing Log Processor...")
    logs = LogProcessor()
    dct = {"ERROR": "Connection timeout"}
    try:
        print(logs.process(dct))
        print("Validation: Log entry verified")
        print(logs.format_output("Output: "), end="\n")
    except Exception as e:
        print(e, end="\n\n")

    print("\n=== Polymorphic Processing Demo ===")
    proc = {
        NumericProcessor(): [1, 2, 3],
        TextProcessor(): "Hello World",
        LogProcessor(): {"INFO": "System ready"}
    }
    print("Processing multiple data types through same interface...")
    for i, p in enumerate(proc):
        p.process(proc[p])
        print(p.format_output(f"Result {i+1}: "), end="\n")
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
