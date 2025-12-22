from pymodbus.client.sync import ModbusTcpClient

def state_discovery_test():
    client = ModbusTcpClient('127.0.0.1', port=5020)
    client.connect()
    
    # RESET: Clear registers 20 and 50 before starting
    client.write_register(20, 0, unit=1)
    client.write_register(50, 0, unit=1)
    
    print("\n--- STARTING STATEFUL DISCOVERY (V3) ---")
    
    print("Step 1: Attempting to write '99' to Reg 50 (SHOULD BE BLOCKED)...")
    client.write_register(50, 99, unit=1)
    res1 = client.read_holding_registers(50, 1, unit=1).registers[0]
    
    print("Step 2: Unlocking via Reg 20...")
    client.write_register(20, 1, unit=1)
    
    print("Step 3: Attempting to write '99' to Reg 50 again (SHOULD WORK)...")
    client.write_register(50, 99, unit=1)
    res2 = client.read_holding_registers(50, 1, unit=1).registers[0]
    
    print("-" * 30)
    print(f"Result 1 (Expected 0): {res1}")
    print(f"Result 2 (Expected 99): {res2}")
    client.close()

if __name__ == "__main__":
    state_discovery_test()