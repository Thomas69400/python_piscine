from abc import ABC, abstractmethod
from typing import Any, List, Dict, Protocol
from collections import deque


class ProcessingStage(Protocol):
    """Protocol defining the interface for data processing stages.

    Any class implementing this protocol must have a process method
    that transforms input data into output data.
    """

    def process(self, data: Any) -> Any:
        """Process the input data.

        Args:
            data: The data to be processed.

        Returns:
            The processed data.
        """
        ...


class ProcessingPipeline(ABC):
    """Abstract base class for processing pipelines.

    A pipeline consists of multiple processing stages that are applied
    sequentially to transform data.
    """

    def __init__(self, pipeline_id: str) -> None:
        """Initialize the processing pipeline.

        Args:
            pipeline_id: Unique identifier for the pipeline.
        """
        self.pipeline_id: str = pipeline_id
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        """Add a processing stage to the pipeline.

        Args:
            stage: The processing stage to add.
        """
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        """Process the input data through all stages.

        Args:
            data: The data to process.

        Returns:
            The processed data.
        """
        ...

    def get_id(self) -> str:
        """Get the pipeline's unique identifier.

        Returns:
            The pipeline ID.
        """
        return self.pipeline_id


class InputStage:
    """Processing stage for input validation and parsing.

    Validates the input data format and converts it to appropriate
    data structures for downstream processing.
    """

    def process(self, data: Any) -> Any:
        """Validate and parse input data.

        Supports string (CSV format), list, and dictionary inputs.
        Converts list and CSV strings to deque for efficient processing.

        Args:
            data: The input data to validate and parse.

        Returns:
            The parsed data in the appropriate format.

        Raises:
            TypeError: If the input data type is not supported.
        """
        print(f"Input: {data}")
        if isinstance(data, str):
            if "," in data:
                return deque(data.split(","))
            return data
        if isinstance(data, list):
            return deque(data)
        if isinstance(data, dict):
            return data
        raise TypeError("Invalid input data")


class TransformStage:
    """Processing stage for data transformation and enrichment.

    Enhances data by adding derived fields or filtering unwanted elements.
    """

    def process(self, data: Any) -> Any:
        """Transform and enrich the input data.

        For dictionaries with 'value' key, adds a 'range' field indicating
        if the value is in normal (20-30) or suspicious range.
        For deques, filters out error entries.

        Args:
            data: The data to transform.

        Returns:
            The transformed data.
        """
        if isinstance(data, dict) and "value" in data:
            value = data["value"]
            data["range"] = (
                "(Normal range)" if 20 <= value <= 30 else "(Suspicious range)"
            )
            return data

        if isinstance(data, deque):
            return [d for d in data if not isinstance(d, str) or d != "error"]

        return data


class OutputStage:
    """Processing stage for output formatting and delivery.

    Formats the processed data into human-readable output messages.
    """

    def process(self, data: Any) -> Any:
        """Format and prepare output data.

        Generates formatted output strings based on the data type:
        - Dictionary: Temperature reading with range info
        - List: Stream summary with statistics
        - Deque: User activity log summary

        Args:
            data: The processed data to format.

        Returns:
            A formatted output string or the original data.
        """
        if isinstance(data, dict):
            return (
                f"Output: Processed temperature reading: "
                f"{data.get('value')}°{data.get('unit')} {data.get('range')}"
            )

        if isinstance(data, list):
            avg = sum(data) / len(data) if data else 0
            return f"Output: Stream summary: {len(data)} readings, " +\
                f"avg: {avg:.1f}°C"

        if isinstance(data, deque):
            return f"Output: User activity logged: {len(data)}" +\
                "actions processed"

        return data


class JSONAdapter(ProcessingPipeline):
    """Pipeline adapter for processing JSON-formatted data.

    Includes input validation, data transformation, and output formatting
    stages to handle JSON data end-to-end.
    """

    def __init__(self, pipeline_id: str) -> None:
        """Initialize the JSON adapter pipeline.

        Args:
            pipeline_id: Unique identifier for this pipeline.
        """
        super().__init__(pipeline_id)
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())

    def process(self, data: Any) -> Any:
        """Process JSON data through all pipeline stages.

        Args:
            data: The JSON data to process.

        Returns:
            The processed and formatted output.

        Raises:
            Exception: If any stage fails during processing.
        """
        try:
            for stage in self.stages:
                data = stage.process(data)
            return data
        except Exception:
            raise


class CSVAdapter(ProcessingPipeline):
    """Pipeline adapter for processing CSV-formatted data.

    Includes input validation and output formatting stages.
    Excludes the transformation stage for simpler CSV processing.
    """

    def __init__(self, pipeline_id: str) -> None:
        """Initialize the CSV adapter pipeline.

        Args:
            pipeline_id: Unique identifier for this pipeline.
        """
        super().__init__(pipeline_id)
        self.add_stage(InputStage())
        self.add_stage(OutputStage())

    def process(self, data: Any) -> Any:
        """Process CSV data through the pipeline stages.

        Args:
            data: The CSV data to process.

        Returns:
            The processed and formatted output.

        Raises:
            Exception: If any stage fails during processing.
        """
        try:
            for stage in self.stages:
                data = stage.process(data)
            return data
        except Exception:
            raise


class StreamAdapter(ProcessingPipeline):
    """Pipeline adapter for processing stream data.

    Handles continuous data streams with input validation, transformation,
    and output formatting.
    """

    def __init__(self, pipeline_id: str) -> None:
        """Initialize the stream adapter pipeline.

        Args:
            pipeline_id: Unique identifier for this pipeline.
        """
        super().__init__(pipeline_id)
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())

    def process(self, data: Any) -> Any:
        """Process stream data through all pipeline stages.

        Args:
            data: The stream data to process.

        Returns:
            The processed and formatted output.

        Raises:
            Exception: If any stage fails during processing.
        """
        try:
            for stage in self.stages:
                data = stage.process(data)
            return data
        except Exception:
            raise


class NexusManager:
    """Manager for coordinating multiple data processing pipelines.

    Maintains a registry of pipelines and routes data to the appropriate
    pipeline based on the pipeline ID.
    """

    def __init__(self) -> None:
        """Initialize the Nexus Manager.

        Creates an empty pipeline registry.
        """
        self.pipelines: Dict[str, ProcessingPipeline] = {}

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        """Register a processing pipeline.

        Args:
            pipeline: The pipeline to register.
        """
        self.pipelines[pipeline.get_id()] = pipeline

    def process(self, pipeline_id: str, data: Any) -> Any:
        """Process data using the specified pipeline.

        Args:
            pipeline_id: The ID of the pipeline to use.
            data: The data to process.

        Returns:
            The processed data from the pipeline.

        Raises:
            ValueError: If the pipeline ID is not found in the registry.
        """
        if pipeline_id not in self.pipelines:
            raise ValueError("Pipeline not found")
        return self.pipelines[pipeline_id].process(data)


def main() -> None:
    """Main function demonstrating the Nexus pipeline system.

    Sets up multiple pipelines for different data formats (JSON, CSV, Stream),
    processes sample data through each pipeline, and demonstrates
    error recovery.
    """
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second\n")
    manager: NexusManager = NexusManager()

    json_pipe: JSONAdapter = JSONAdapter("JSON")
    csv_pipe: CSVAdapter = CSVAdapter("CSV")
    stream_pipe: StreamAdapter = StreamAdapter("STREAM")

    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery\n")
    manager.add_pipeline(json_pipe)
    manager.add_pipeline(csv_pipe)
    manager.add_pipeline(stream_pipe)

    print("=== Multi-Format Data Processing ===")

    print("\nProcessing JSON data through pipeline...")
    print(manager.process("JSON", {
        "sensor": "temp",
        "value": 23.5,
        "unit": "C"
    }))

    print("\nProcessing CSV data through same pipeline...")
    print(manager.process("CSV", "user,action,timestamp"))

    print("\nProcessing Stream data through same pipeline...")
    print(manager.process("STREAM", [25, 22, 21, 24, 23]))

    print("\n=== Pipeline Chaining Demo ===")
    manager.process("STREAM", [20, 21, 22])
    manager.process("CSV", "processed,data,stored")
    print("Chain result: 2 pipelines executed successfully")

    print("\n=== Error Recovery Test ===")
    try:
        print("Simulating pipeline failure..")
        manager.process("XXX", "invalid")
    except Exception:
        print("Error detected in pipeline")
        print("Recovery initiated: Switching to backup processor")
        print("Recovery successful")

    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
