from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, s_id: str, s_type: str) -> None:
        super().__init__()
        self.stats: Dict[str, Union[str, int, float]] = dict()
        self.s_id: str = s_id
        self.s_type: str = s_type

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return self.stats

    def display_base_data(self) -> None:
        print(f"Stream ID: {self.s_id}, Type: {self.s_type}")


class SensorStream(DataStream):
    def __init__(self, s_id: str) -> None:
        super().__init__(s_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
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
        tmp = list(self.stats[temp]
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
        if criteria is not None:
            if criteria == "High-priority":
                try:
                    filtered = [
                        data
                        for data
                        in data_batch
                        if "temp" or "humidity" in data
                        and float(data.split(":")[1]) > 50
                    ]
                    return filtered
                except ValueError as e:
                    raise ValueError(f"Error filtering sensor data: {e}")
        return data_batch


class TransactionStream(DataStream):
    def __init__(self, s_id: str) -> None:
        super().__init__(s_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
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
        buy = sum([
            self.stats[buy]
            for buy
            in self.stats
            if "buy" in buy
        ])
        sell = sum([
            self.stats[buy]
            for buy
            in self.stats
            if "sell" in buy
        ])
        symbol = ""
        if buy - sell > 0:
            symbol = "+"
        return result + f"{len(self.stats)} operations, " + \
            f"net flow: {symbol}{buy - sell} units"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        if criteria is not None:
            if criteria == "High-priority":
                try:
                    filtered = [
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
    def __init__(self, s_id: str) -> None:
        super().__init__(s_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
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
        ope = len(self.stats)
        n_error = len([
            self.stats[error]
            for error
            in self.stats
            if self.stats[error] == "error"
        ])
        return result + f"{ope} events, " + \
            f"{n_error} error detected"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        if criteria is not None:
            if criteria == "High-priority":
                try:
                    filtered = [
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
    def __init__(self) -> None:
        pass

    def process_stream(streams: Dict[Union[EventStream,
                                           TransactionStream,
                                           SensorStream],
                                     Union[str,
                                           float,
                                           int]],
                       criteria: Optional[str] = None) -> str:
        sensor = 0
        trans = 0
        event = 0
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
                to_return = "Filtered results: "
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
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    sensor.display_base_data()
    sens_data = ["temp:22.5", "humidity:65", "pressure:1013"]
    try:
        print(sensor.process_batch(sens_data))
        print(sensor.format_output("Sensor analysis: "))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nInitializing Transaction Stream...")
    trans = TransactionStream("TRANS_001")
    trans.display_base_data()
    trans_data = ["buy:100", "sell:150", "buy:75"]
    try:
        print(trans.process_batch(trans_data))
        print(trans.format_output("Transaction analysis: "))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    event_data = ["login", "error", "logout"]
    event.display_base_data()
    try:
        print(event.process_batch(event_data))
        print(event.format_output("Event analysis: "))
    except Exception as e:
        print(f"Error: {e}")

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    streams = {
        SensorStream("SENSOR_002"): ["temp:50",
                                     "humidity:70"],
        TransactionStream("TRANS_002"): ["buy:50",
                                         "buy:1000",
                                         "sell:250",
                                         "buy:100"],
        EventStream("EVENT_002"): ["login", "logout", "login"]
    }
    try:
        print(StreamProcessor.process_stream(streams))
    except ValueError as e:
        print(f"Error: {e}")

    streams_priority = {
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
        print(StreamProcessor.process_stream(
            streams_priority, "High-priority"))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
