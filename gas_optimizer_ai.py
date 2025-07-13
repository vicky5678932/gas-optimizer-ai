import json
import random
from web3 import Web3

def estimate_gas_cost(tx_data):
    """Estimate gas cost based on tx complexity."""
    base = 21000
    complexity = len(json.dumps(tx_data)) // 10
    fluctuation = random.randint(1000, 4000)
    return base + complexity + fluctuation

if __name__ == "__main__":
    sample_tx = {"to": "0x0", "value": 1000000000000000000, "data": "0x"}
    estimated_cost = estimate_gas_cost(sample_tx)
    print(f"Estimated gas: {estimated_cost}")
