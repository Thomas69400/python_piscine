from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Abstract base class representing a generic data stream.

    Subclasses must implement process_batch to handle a batch of data.
    """

    def __init__(self, s_id: str, s_type: str) -> None:
        """Initialize DataStream

        Args:
            s_id (str): the id of stream
            s_type (str): the type of stream
        """

        super().__init__()
        self.stats: Dict[str, Union[str, int, float]] = dict()
        self.s_id: str = s_id
        self.s_type: str = s_type

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process the data

        Args:
            data_batch (List[Any]): the data to process

        Returns:
            str: The data processed
        """

        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        """Filter data depending on optional criteria

        Args:
            data_batch (List[Any]): the data to filter
            criteria (Optional[str], optional): criteria to filter on.
                Defaults to None.

        Returns:
            List[Any]: the data filtered
        """

        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return the stats of stream

        Returns:
            Dict[str, Union[str, int, float]]: the data of stream
        """

        return self.stats

    def display_base_data(self) -> None:
        """Print the ID and Type of stream"""

        print(f"Stream ID: {self.s_id}, Type: {self.s_type}")


class SensorStream(DataStream):
    """Stream handling environmental sensor readings.

    SensorStream parses key:value strings (e.g., "temp:22.5") and stores
    parsed numeric stats in self.stats.
    """

    def __init__(self, s_id: str) -> None:
        """Initialize a SensorStream

        Args:
            s_id (str): the id
        """

        super().__init__(s_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process the data

        Args:
            data_batch (List[Any]): the data to process

        Returns:
            str: The data processed
        """

        if not isinstance(data_batch, list):
            raise TypeError("Error SensorStream data is not a list")
        try:
            self.stats = {
                splited[0]: float(splited[1])
                for splited
                in [
                    data.split(":")
                    for data
                    in data_batch
                ]
            }
        except ValueError as e:
            raise ValueError(f"Processing sensor: {e}")
        return f"Processing sensor batch: {data_batch}"

    def format_output(self, result: str) -> str:
        """Filter data depending on optional criteria

        Args:
            data_batch (List[Any]): the data to filter
            criteria (Optional[str], optional): criteria to filter on.
                Defaults to None.

        Returns:
            List[Any]: the data filtered
        """

        tmp: Union[List[float], str] = list(self.stats[temp]
                                            for temp
                                            in self.stats
                                            if temp == 'temp')
        if len(tmp) == 0:
            tmp = "No temp"
        else:
            tmp = str(tmp[0]) + "°C"
        return result + f"{len(self.stats)} readings processed, " + \
            f"avg temp: {tmp}"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        """Filter data depending on optional criteria

        Args:
            data_batch (List[Any]): the data to filter
            criteria (Optional[str], optional): criteria to filter on.
                Defaults to None.

        Returns:
            List[Any]: the data filtered
        """

        if criteria is not None:
            if criteria == "High-priority":
                try:
                    filtered: List[float] = [
                        data
                        for data
                        in data_batch
                        if ("temp" or "humidity" in data)
                        and float(data.split(":")[1]) > 50
                    ]
                    return filtered
                except ValueError as e:
                    raise ValueError(f"Error filtering sensor data: {e}")
        return data_batch


class TransactionStream(DataStream):
    """Stream handling financial transaction records.

    TransactionStream parses key:value strings (e.g., "buy:100") and stores
    integer values of operations in self.stats with enumerated keys.
    """

    def __init__(self, s_id: str) -> None:
        """Initialize a TransactionStream

        Args:
            s_id (str): id of stream
        """

        super().__init__(s_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process the data

        Args:
            data_batch (List[Any]): the data to process

        Returns:
            str: The data processed
        """

        if not isinstance(data_batch, list):
            raise TypeError(
                "Error TransactionStream data is not a list")
        try:
            self.stats = {
                f"{splited[0]}_{i}": int(splited[1])
                for i, splited
                in enumerate([
                    data.split(":")
                    for data
                    in data_batch
                ])
            }
        except ValueError as e:
            raise ValueError(f"Error processing transaction: {e}")
        return f"Processing transaction batch: {data_batch}"

    def format_output(self, result: str) -> str:
        """Filter data depending on optional criteria

        Args:
            data_batch (List[Any]): the data to filter
            criteria (Optional[str], optional): criteria to filter on.
                Defaults to None.

        Returns:
            List[Any]: the data filtered
        """

        buy: int = sum([
            self.stats[buy]
            for buy
            in self.stats
            if "buy" in buy
        ])
        sell: int = sum([
            self.stats[buy]
            for buy
            in self.stats
            if "sell" in buy
        ])
        symbol: str = ""
        if buy - sell > 0:
            symbol = "+"
        return result + f"{len(self.stats)} operations, " + \
            f"net flow: {symbol}{buy - sell} units"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        """Filter data depending on optional criteria

        Args:
            data_batch (List[Any]): the data to filter
            criteria (Optional[str], optional): criteria to filter on.
                Defaults to None.

        Returns:
            List[Any]: the data filtered
        """

        if criteria is not None:
            if criteria == "High-priority":
                try:
                    filtered: List[int] = [
                        data
                        for data
                        in data_batch
                        if float(data.split(":")[1]) > 500
                    ]
                    return filtered
                except ValueError as e:
                    raise ValueError(f"Error filtering transaction data: {e}")
        return data_batch


class EventStream(DataStream):
    """Stream handling system event records.

    EventStream stores each event from the batch into self.stats using
    event_<n> keys and supports simple event-based reporting.
    """

    def __init__(self, s_id: str) -> None:
        """Initialize an EventStream

        Args:
            s_id (str): id of stream
        """

        super().__init__(s_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process the data

        Args:
            data_batch (List[Any]): the data to process

        Returns:
            str: The data processed
        """

        if not isinstance(data_batch, list):
            raise TypeError("Error EventStream data is not a list")
        try:
            self.stats.update({
                f"event_{i+1}": data
                for i, data
                in enumerate(data_batch)
            })
        except ValueError as e:
            raise ValueError(f"Error processing event: {e}")
        return f"Processing event batch: {data_batch}"

    def format_output(self, result: str) -> str:
        """Filter data depending on optional criteria

        Args:
            data_batch (List[Any]): the data to filter
            criteria (Optional[str], optional): criteria to filter on.
                Defaults to None.

        Returns:
            List[Any]: the data filtered
        """

        ope: int = len(self.stats)
        n_error: int = len([
            self.stats[error]
            for error
            in self.stats
            if self.stats[error] == "error"
        ])
        return result + f"{ope} events, " + \
            f"{n_error} error detected"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        """Filter data depending on optional criteria

        Args:
            data_batch (List[Any]): the data to filter
            criteria (Optional[str], optional): criteria to filter on.
                Defaults to None.

        Returns:
            List[Any]: the data filtered
        """

        if criteria is not None:
            if criteria == "High-priority":
                try:
                    filtered: List[str] = [
                        data
                        for data
                        in data_batch
                        if data == "error"
                    ]
                    return filtered
                except ValueError as e:
                    raise ValueError(f"Error filtering event data: {e}")
        return data_batch


class StreamProcessor:
    """Coordinator for processing multiple DataStream instances.

    Accepts a mapping of DataStream -> list of raw batch items and applies
    filtering and processing for each registered stream.
    """

    def __init__(self) -> None:
        """Initialize a StreamProcessor instance."""

        pass

    def process_stream(self, streams: Dict[DataStream,
                                           List[Any]],
                       criteria: Optional[str] = None) -> str:
        """Process all streams

        Args:
            streams (Dict[Union[EventStream, TransactionStream, SensorStream],
                Union[str, float, int]]): the streams to process
            criteria (Optional[str], optional): the criteria to
                filter the data. Defaults to None.

        Raises:
            ValueError: if data can't be parsed

        Returns:
            str: a description of processed data
        """

        sensor: int = 0
        trans: int = 0
        event: int = 0
        for s in streams:
            try:
                streams[s] = s.filter_data(streams[s], criteria)
                s.process_batch(streams[s])
                if isinstance(s, SensorStream):
                    sensor += len(s.get_stats())
                if isinstance(s, TransactionStream):
                    trans += len(s.get_stats())
                if isinstance(s, EventStream):
                    event += len(s.get_stats())
            except ValueError as e:
                raise ValueError(f"Error: {e}")
        if criteria is not None:
            if criteria == "High-priority":
                to_return: str = "Filtered results: "
                if sensor != 0:
                    to_return += f"{sensor} critical sensor alerts"
                if trans != 0:
                    to_return += f", {trans} large transaction"
                if event != 0:
                    to_return += f", {event} error detected"
                return to_return
        return "Batch 1 Results:\n" + \
            f"- Sensor data: {sensor} readings processed\n" + \
            f"- Transaction data: {trans} operations processed\n" + \
            f"- Event data: {event} events processed"


def main() -> None:
    """Execute program"""

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor: SensorStream = SensorStream("SENSOR_001")
    sensor.display_base_data()
    sens_data: List[str] = ["temp:22.5", "humidity:65", "pressure:1013"]
    try:
        print(sensor.process_batch(sens_data))
        print(sensor.format_output("Sensor analysis: "))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nInitializing Transaction Stream...")
    trans: TransactionStream = TransactionStream("TRANS_001")
    trans.display_base_data()
    trans_data: List[str] = ["buy:100", "sell:150", "buy:75"]
    try:
        print(trans.process_batch(trans_data))
        print(trans.format_output("Transaction analysis: "))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nInitializing Event Stream...")
    event: EventStream = EventStream("EVENT_001")
    event_data: List[str] = ["login", "error", "logout"]
    event.display_base_data()
    try:
        print(event.process_batch(event_data))
        print(event.format_output("Event analysis: "))
    except Exception as e:
        print(f"Error: {e}")

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    proc: StreamProcessor = StreamProcessor()
    streams: Dict[DataStream, List[str]] = {
        SensorStream("SENSOR_002"): ["temp:50",
                                     "humidity:70"],
        TransactionStream("TRANS_002"): ["buy:50",
                                         "buy:1000",
                                         "sell:250",
                                         "buy:100"],
        EventStream("EVENT_002"): ["login", "logout", "login"]
    }
    try:
        print(proc.process_stream(streams))
    except ValueError as e:
        print(f"Error: {e}")

    streams_priority: Dict[DataStream, List[str]] = {
        SensorStream("SENSOR_003"): ["temp:50",
                                     "humidity:70"],
        TransactionStream("TRANS_003"): ["buy:50",
                                         "buy:1000",
                                         "sell:250",
                                         "buy:100"],
        EventStream("EVENT_003"): ["login", "logout", "login"]
    }
    print("\nStream filtering active: High-priority data only")
    try:
        print(proc.process_stream(
            streams_priority, "High-priority"))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
