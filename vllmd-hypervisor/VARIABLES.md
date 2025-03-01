# VLLMD Hypervisor Variables

This document provides a comprehensive list of variables used in the VLLMD Hypervisor system, organized by scope with their data types and purposes clearly defined.

## Global Variables

| Variable | Scope | Data Type | Purpose |
|----------|-------|-----------|---------|
| `VLLMD_HYPERVISOR_AUTO_YES` | Global | Boolean | Automatically accepts default values without prompting user |
| `VLLMD_HYPERVISOR_CLOUDINIT_FILEPATH` | Global | String | Path to cloud-init configuration disk |
| `VLLMD_HYPERVISOR_CREATED_FILEPATH_LIST` | Global | Array | List of file paths created during script execution |
| `VLLMD_HYPERVISOR_DRY_RUN` | Global | Boolean | Controls whether actions are executed or only simulated for preview |
| `VLLMD_HYPERVISOR_GPU_ADDRESS_LIST` | Global | Array | List of detected GPU PCI addresses |
| `VLLMD_HYPERVISOR_NETWORK_BRIDGE_NAME` | Global | String | Name of the bridge interface for VM networking |
| `VLLMD_HYPERVISOR_NETWORK_DEFAULT_INTERFACE` | Global | String | Default host network interface to use for VM connectivity |
| `VLLMD_HYPERVISOR_RUNTIME_CONFIG_FILEPATH` | Global | String | Path to the TOML runtime configuration file |
| `VLLMD_HYPERVISOR_RUNTIME_COUNT` | Global | Integer | Number of configured runtimes |
| `VLLMD_HYPERVISOR_RUNTIME_INDEX_LIST` | Global | Array | List of runtime indices defined in configuration |
| `VLLMD_HYPERVISOR_RUNTIME_NAME_LIST` | Global | Array | List of runtime names defined in configuration |
| `VLLMD_HYPERVISOR_STEP_COUNT` | Global | Integer | Tracks current step count for dry run output |
| `VLLMD_HYPERVISOR_USER` | Global | String | Username for systemd services |
| `VLLMD_HYPERVISOR_VALIDATION_MODE` | Global | String | Schema validation mode (strict or lenient) |

## Global Constants

| Variable | Scope | Data Type | Purpose |
|----------|-------|-----------|---------|
| `VLLMD_HYPERVISOR_CONFIG_PATH` | Global/Const | String | Path to VLLMD configuration directory |
| `VLLMD_HYPERVISOR_DEFAULT_CPUS` | Global/Const | Integer | Default CPU allocation per runtime if not specified |
| `VLLMD_HYPERVISOR_DEFAULT_MEMORY_GIB` | Global/Const | Integer | Default memory allocation per runtime in GiB |
| `VLLMD_HYPERVISOR_IMAGE_PATH` | Global/Const | String | Path to VM image storage directory |
| `VLLMD_HYPERVISOR_LOG_PATH` | Global/Const | String | Path to VLLMD log directory |
| `VLLMD_HYPERVISOR_MAXIMUM_MEMORY_GIB` | Global/Const | Integer | Maximum memory allocation per runtime in GiB |
| `VLLMD_HYPERVISOR_MINIMUM_MEMORY_GIB` | Global/Const | Integer | Minimum memory allocation per runtime in GiB |
| `VLLMD_HYPERVISOR_SCHEMA_FILEPATH` | Global/Const | String | Path to JSON schema file for configuration validation |
| `VLLMD_HYPERVISOR_STATE_PATH` | Global/Const | String | Path to VLLMD state directory |
| `VLLMD_HYPERVISOR_SYSTEMD_PATH` | Global/Const | String | Path to systemd user service directory |

## Runtime Configuration Variables

| Variable | Scope | Data Type | Purpose |
|----------|-------|-----------|---------|
| `VLLMD_HYPERVISOR_CPUS` | Runtime Config | Integer | Number of CPU cores allocated to the runtime |
| `VLLMD_HYPERVISOR_GPU_DEVICE_LIST` | Runtime Config | Array | List of PCI addresses of GPUs assigned to the runtime |
| `VLLMD_HYPERVISOR_INDEX` | Runtime Config | Integer | Unique index for the runtime (used in systemd service names) |
| `VLLMD_HYPERVISOR_MEMORY_GIB` | Runtime Config | Integer | Memory allocation for runtime in GiB |
| `VLLMD_HYPERVISOR_NAME` | Runtime Config | String | Descriptive name for the runtime |

## Runtime Execution Variables

| Variable | Scope | Data Type | Purpose |
|----------|-------|-----------|---------|
| `VLLMD_HYPERVISOR_LOG_FILEPATH` | Runtime | String | Path to runtime's log file |
| `VLLMD_HYPERVISOR_RUNTIME_PATH` | Runtime | String | Path to runtime's directory |

## Function Local Variables

| Variable | Scope | Data Type | Purpose |
|----------|-------|-----------|---------|
| `config_filepath` | Function Local | String | Path to runtime configuration file |
| `current_interface` | Function Local | String | Current network interface name being processed |
| `gpu_address` | Function Local | String | PCI address of GPU in processing |
| `jsonschema_installed` | Function Local | Boolean | Flag indicating if jsonschema Python package is installed |
| `memory_gib` | Function Local | Integer | Memory allocation for runtime in GiB |
| `runtime_index` | Function Local | Integer | Index of the current runtime being processed |
| `runtime_name` | Function Local | String | Name of the current runtime being processed |
| `schema_version` | Function Local | String | Version of the schema definition being used |
| `service_name` | Function Local | String | Name of the systemd service being configured |
| `tomli_installed` | Function Local | Boolean | Flag indicating if tomli/tomllib Python package is installed |
| `validation_result` | Function Local | Integer | Exit code of the validation process |

## Variable Scopes

- **Global**: Available throughout the script, can be modified
- **Global/Const**: Global constant, defined once and never modified
- **Runtime Config**: Used in runtime configuration files
- **Runtime**: Created or used during runtime execution
- **Function Local**: Scoped to a specific function (can be mutable or constant)

<!--
# Instructions for updating this file

1. NAMING CONVENTION:
   - All global and constant variables MUST be prefixed with `VLLMD_HYPERVISOR_`
   - All path variables MUST end with `_PATH`
   - All file path variables MUST end with `_FILEPATH`
   - All array/collection variables MUST end with `_LIST`
   - All count variables MUST end with `_COUNT` (avoid abbreviations)
   - Replace MIN/MAX with MINIMUM/MAXIMUM for clarity
   - Memory values MUST use `GiB` (not GB) for binary units
   - Use `Boolean` type for flags/toggles (not Integer)
   - Function-local variables MAY use shorter, more concise names
   - Variable names MUST be as explicit and unambiguous as possible

2. ORGANIZATION:
   - Variables MUST be sorted by:
     1. Scope (Global, Global/Const, Runtime Config, Runtime, Function Local)
     2. Alphabetically by name within each scope
   - Table columns: Variable, Scope, Data Type, Purpose
   - Data types MUST be specific (Boolean, Integer, String, Array, etc.)

3. SCOPE DEFINITIONS:
   - Global: Available throughout the script, can be modified
   - Global/Const: Global constant, defined once and never modified
   - Runtime Config: Used in runtime configuration files
   - Runtime: Created or used during runtime execution
   - Function Local: Scoped to a specific function (can be mutable or constant)

4. VARIABLE PURPOSES:
   - Purpose descriptions MUST be clear, concise, and unambiguous
   - Focus on what the variable represents, not implementation details
   - Include SI units for numeric values (GiB, MHz, etc.)
   - For related variables (like RUNTIME_INDEX_LIST vs RUNTIME_NAME_LIST), 
     clearly explain their relationship and differences
   - Avoid vague descriptions that could lead to programmer confusion

## Instruction Tuning

This document serves as the definitive reference for variable naming and usage in the VLLMD Hypervisor system. To maintain its integrity and usefulness:

1. **Completeness**: Every variable used in the VLLMD Hypervisor system MUST be documented here before being introduced to the codebase.

2. **Variable Addition Process**:
   - Add the variable to this document first
   - Fill in all four columns: Variable, Scope, Data Type, Purpose
   - Ensure the variable follows established naming conventions
   - Place the variable in the correct scope section
   - Sort alphabetically within its scope section

3. **Variable Modification Process**:
   - Update this document before changing variable names in code
   - Document the old name alongside the new name temporarily
   - After code changes are complete, remove the old name reference

4. **Documentation Accuracy Verification**:
   - Run a quarterly audit to ensure all variables in code match this document
   - Verify that variable purposes match actual usage
   - Update variable descriptions to reflect any changes in functionality

5. **Reviewing Variable Additions**:
   - Check for naming convention compliance
   - Verify scope is correctly identified
   - Ensure data type is specific and accurate
   - Confirm purpose is clear, concise, and unambiguous
   - Look for potential name conflicts or confusing similarities

6. **Schema Compliance**:
   - Ensure variables align with the JSON Schema definition in `vllmd-hypervisor-config-schema.json`
   - Variables used for configuration should reflect the schema structure
   - Follow schema validation requirements for data types and constraints

7. **Advanced Usage**:
   - Use this document as a tool for static analysis
   - Generate code linting rules from these conventions
   - Reference when creating new components that need to interact with existing variables

This document should be treated as a living specification - keep it current as the system evolves, and reference it during code reviews to maintain consistent variable usage throughout the codebase.

When updating this file, maintain this comment section to preserve these instructions.
-->