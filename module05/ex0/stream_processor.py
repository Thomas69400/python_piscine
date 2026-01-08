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

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        if not self.validate(data):
            raise ValueError("Invalid data for NumericProcessor")
        count = len(data)
        total = sum(data)
        avg = total/count
        return f"Processed {count} numeric values, sum={total}, avg={avg}"

    def validate(self, data: Any) -> bool:
        try:
            assert isinstance(data, int) or (
                isinstance(data, list) and all(isinstance(x, int)
                                               for x in data)
            )
            print("Validation: Numeric data verified")
            return True
        except AssertionError:
            print("Error: Data must be an int or a list of ints")
        return False

    def format_output(self, result: str) -> str:
        return f"{result}"


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        print(f"Processing data: \"{data}\"")
        if not self.validate(data):
            raise ValueError("Invalid data for TextProcessor")
        length = len(data)
        words = len(data.split())
        return f"Processed text: {length} characters, {words} words"

    def validate(self, data: Any) -> bool:
        try:
            assert isinstance(data, str)
            print("Validation: Text data verified")
            return True
        except AssertionError:
            print("Error: Data must be a string.")
        return False

    def format_output(self, result: str) -> str:
        return f"{result}"


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        if not self.validate(data):
            raise ValueError("Invalid data for LogProcessor")
        for key in data:
            if key == "ERROR":
                return f"[ALERT] ERROR level detected: {data[key]}"
            else:
                return f"[INFO] INFO level detected: {data[key]}"

    def validate(self, data: Any) -> bool:
        try:
            assert isinstance(data, dict)
            print("Validation: Log entry verified")
            return True
        except AssertionError as e:
            print(f"Error: {e}")
        return False

    def format_output(self, result: str) -> str:
        return f"{result}"


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    nume = NumericProcessor()
    lst = [1, 2, 3, 4, 5, "test"]
    try:
        print("Output: " + nume.format_output(nume.process(lst)), end="\n\n")
    except Exception as e:
        print(e, end="\n\n")

    print("Initializing Text Processor...")
    txt = TextProcessor()
    s = "Hello Nexus World"
    try:
        print("Output: " + txt.format_output(txt.process(s)), end="\n\n")
    except Exception as e:
        print(e, end="\n\n")

    print("Initializing Log Processor...")
    logs = LogProcessor()
    dct = {"ERROR": "Connection timeout"}
    try:
        print("Output: " + logs.format_output(logs.process(dct)), end="\n")
    except Exception as e:
        print(e, end="\n\n")

    print("\n=== Polymorphic Processing Demo ===")
    proc = {
        NumericProcessor(): [1, 2, 3],
        TextProcessor(): "Hello World",
        LogProcessor(): {"INFO": "System ready"}
    }
    for i, p in enumerate(proc):
        print(f"Result {i+1}: " + p.process(proc[p]), end="\n")
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
