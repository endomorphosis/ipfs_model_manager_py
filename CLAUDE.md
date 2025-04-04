# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build and Installation
- Install: `pip install .`
- Run tests: `python test.py`
- Run single test: `python -m ipfs_model_manager_py.test.test_fio`
- Run example: `python example.py`


### Build & Test Commands
- **Install**: `pip install -e .`
- **Build**: `python setup.py build`
- **Run all tests**: `python -m test.test`
- **Run single test**: `python -m test.test_ipfs_kit` or `python -m test.test_storacha_kit`
- **Run API server**: `uvicorn ipfs_kit_py.api:app --reload --port 8000`
- **Generate AST**: `python -m astroid ipfs_kit_py > ast_analysis.json`
- **Check for duplications**: `pylint --disable=all --enable=duplicate-code ipfs_kit_py`

### Development Guidelines
- **Test-First Development**: All new features must first be developed in the test/ folder
- **Feature Isolation**: Do not modify code outside of test/ until fully debugged
- **API Exposure**: All functionality should be exposed via FastAPI endpoints
- **Performance Focus**: Use memory-mapped structures and Arrow C Data Interface for low-latency IPC
- **Code Analysis**: Maintain an abstract syntax tree (AST) of the project to identify and prevent code duplication
- **DRY Principle**: Use the AST to enforce Don't Repeat Yourself by detecting similar code structures

### Testing Strategy

The project follows a comprehensive testing approach to ensure reliability and maintainability:

#### Test Organization
- **Unit Tests**: Located in the `test/` directory with file naming pattern `test_*.py`
- **Integration Tests**: Also in `test/` but focused on component interactions
- **Performance Tests**: Specialized tests for measuring throughput and latency

#### Recent Test Improvements
- **Mock Integration**: Fixed PyArrow mocking for cluster state helpers
- **Role-Based Architecture**: Improved fixtures for master/worker/leecher node testing
- **Gateway Compatibility**: Enhanced testing with proper filesystem interface mocking
- **LibP2P Integration**: Fixed tests to work without external dependencies
- **Parameter Validation**: Corrected constructor argument handling in tests
- **Interface Focus**: Made tests more resilient to implementation changes by focusing on behaviors rather than implementation details

#### Test Patterns
1. **Fixture-Based Testing**: Use pytest fixtures for test setup and teardown
2. **Mocking IPFS Daemon**: Use subprocess mocking to avoid actual daemon dependency
3. **Property-Based Testing**: Use hypothesis for edge case discovery
4. **Snapshot Testing**: For configuration and schema verification
5. **Parallelized Test Execution**: For faster feedback cycles
6. **PyArrow Patching**: Special handling for PyArrow Schema objects and Table methods
7. **Logging Suppression**: Context managers to control test output noise

#### PyArrow Testing Strategy
The tests must handle PyArrow's immutable Schema objects during mocking. Key approaches:

1. **MonkeyPatching**: Using pytest's monkeypatch fixture to safely patch immutable types
2. **Schema Equality Override**: Custom equality checks that handle MagicMock objects
3. **Schema Type Conversion**: Automatic conversion from MagicMock schemas to real PyArrow schemas
4. **Error Handling**: Special handling for PyArrow's strict type checking errors
5. **Cleanup Patching**: Custom cleanup methods to prevent errors during test teardown

#### Continuous Integration Integration
- Tests are run on every PR and commit to main branch
- Test reports and coverage metrics are generated automatically
- Performance regression tests compare against baseline benchmarks

## Code Style Guidelines
- **Imports**: Standard library first, third-party next, project imports last
- **Variables/Functions**: Use snake_case
- **Classes**: Use snake_case (this is project-specific, differs from PEP 8)
- **Indentation**: 4 spaces, no tabs
- **Error Handling**: Use try/except blocks, catch specific exceptions when possible
- **No Type Annotations**: Project doesn't use typing hints
- **Docstrings**: Not consistently used

The project is a wrapper around HuggingFace Transformers that adds IPFS model management capabilities, allowing models to be downloaded from HTTP/S3/IPFS based on availability and speed.

### API Integration Points
- **IPFS HTTP API**: REST interface (localhost:5001/api/v0) for core IPFS operations
- **IPFS Cluster API**: REST interface (localhost:9094/api/v0) for cluster coordination
- **IPFS Cluster Proxy**: Proxied IPFS API (localhost:9095/api/v0)
- **IPFS Gateway**: Content retrieval via HTTP (localhost:8080/ipfs/[cid])
- **IPFS Socket Interface**: Unix socket for high-performance local communication (/ip4/127.0.0.1/tcp/4001)
- **IPFS Unix Socket API**: On Linux, Kubo can be configured to expose its API via a Unix domain socket instead of HTTP, providing lower-latency communication for local processes. This can be configured in the IPFS config file by modifying the `API.Addresses` field to include a Unix socket path (e.g., `/unix/path/to/socket`).

These APIs enable creating "swarms of swarms" by allowing distributed clusters to communicate across networks and coordinate content pinning, replication, and routing across organizational boundaries. Socket interfaces provide lower-latency communication for high-performance local operations, with Unix domain sockets being particularly efficient for inter-process communication on the same machine.

## IPFS Core Concepts

The IPFS (InterPlanetary File System) architecture is built on several key concepts and components that are essential to understand for effective implementation:

### Content Addressing
- **Content Identifiers (CIDs)**: Unique fingerprints of content based on cryptographic hashes
- **Multihash Format**: Extensible hashing format supporting multiple hash algorithms (default: SHA-256)
- **Base32/Base58 Encoding**: Human-readable representations of binary CIDs
- **Version Prefixes**: CIDv0 (base58btc-encoded SHA-256) vs CIDv1 (self-describing, supports multicodec)

### Data Structures
- **Merkle DAG (Directed Acyclic Graph)**: Core data structure for content-addressed storage
- **IPLD (InterPlanetary Linked Data)**: Framework for creating data models with content-addressable linking
- **UnixFS**: File system abstraction built on IPLD for representing traditional files/directories
- **Blocks**: Raw data chunks that form the atomic units of the Merkle DAG

### Network Components
- **DHT (Distributed Hash Table)**: Distributed key-value store for content routing
- **Bitswap**: Protocol for exchanging blocks between peers
- **libp2p**: Modular networking stack powering IPFS peer-to-peer communication
- **MultiFormats**: Self-describing protocols, formats, and addressing schemes
- **IPNS (InterPlanetary Name System)**: Mutable naming system for content addressing

### Node Types
- **Full Nodes**: Store and serve content, participate in DHT
- **Gateway Nodes**: Provide HTTP access to IPFS content
- **Client Nodes**: Lightweight nodes that rely on others for content routing/storage
- **Bootstrap Nodes**: Well-known nodes that help new nodes join the network
- **Relay Nodes**: Assist with NAT traversal and indirect connections

### Key Operations
- **Adding Content**: Hash-based deduplication and chunking strategies
- **Retrieving Content**: Resolution process from CID to data
- **Pinning**: Mechanism to prevent content from being garbage collected
- **Publishing**: Making content discoverable through DHT/IPNS
- **Garbage Collection**: Process for reclaiming storage from unpinned content

## Code Style Guidelines
- Imports: Standard library first, followed by third-party, then local imports
- Error handling: Use try/except blocks for imports and API calls
- Variable naming: snake_case for variables and functions, PascalCase for classes
- Types: Type annotations preferred but not mandatory
- Formatting: 4-space indentation, no trailing whitespace
- Error handling: Catch specific exceptions where possible
- Async: Use asyncio for asynchronous operations
- Comments: Document complex operations, especially when working with IPFS
- Environment handling: Check for user permissions with os.geteuid()
- File structure: Keep related functionality in the same module
- Logging: Use print statements for simple debugging

## Architecture Notes
This project manages HuggingFace models using IPFS, S3, and local storage backends.