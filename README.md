# ModbusDiff: State-Aware Protocol Differential Fuzzer

## Overview
This project is a research testbed designed to identify Semantic Gaps and Stateful Logic Vulnerabilities in the Modbus/TCP protocol. It was inspired by research in protocol differential testing (e.g., BLEDiff, DIKEUE).

## Key Research Findings
1. Address Offset Discrepancies: Identified a `+1` indexing shift between Master and Slave implementations that can lead to security policy bypass.
2. Semantic Boundary Gaps: Demonstrated how unsigned 16-bit integers (65535) can be misinterpreted as signed integers (-1) to bypass range checks.
3. State-Dependent Access Control: Implemented and verified a "Hidden State" interlock where Register 50 permissions depend on the value of Register 20.

## Tools
 `sim_slave.py`: A custom state-aware Modbus simulator (The Target).
 `modbus_diff.py`: An automated auditor used for state discovery and compliance mapping.
