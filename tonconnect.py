# Simulated TonConnect integration for demonstration

class TonConnect:
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def send_ton(self, user_id, amount):
        # Simulated transaction logic
        print(f"Sending {amount} TON to {self.wallet_address} for user {user_id}")
        return {'status': 'success'}