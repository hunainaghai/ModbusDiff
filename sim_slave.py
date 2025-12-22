from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext

class StatefulDataBlock(ModbusSequentialDataBlock):
    def setValues(self, address, values):
        # Based on your logs, the client 'Reg 20' is actually 'Address 21'
        # So we check the lock status at index 21
        all_values = self.values 
        lock_status = all_values[21] 
        
        # We align our security check to Address 51 (which is client Reg 50)
        if address == 51 and lock_status == 0:
            print(f"!!! SUCCESSFUL BLOCK: Write to {address} rejected because Reg 21 is {lock_status} !!!")
            return 
            
        if address == 51 and lock_status == 1:
            print(f"!!! SUCCESSFUL ALLOW: Write to {address} accepted because Reg 21 is {lock_status} !!!")

        super().setValues(address, values)

store = ModbusSlaveContext(hr=StatefulDataBlock(0, [0]*100))
context = ModbusServerContext(slaves=store, single=True)
print("--- STATEFUL SIMULATOR (V5) STARTING ---")
StartTcpServer(context, address=("127.0.0.1", 5020))