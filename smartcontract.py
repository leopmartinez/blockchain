class SmartContract:
    def __init__(self, client, freelancer, payment_amount):
        self.client = client
        self.freelancer = freelancer
        self.payment_amount = payment_amount
        self.job_done = False
        self.payment_released = False
    
    def mark_job_done(self):
        if self.job_done:
            print("Job is already marked as done.")
        else:
            self.job_done = True
            print("Job marked as done.")

    def release_payment(self):
        if not self.job_done:
            print("Cannot release payment. Job is not marked as done.")
        elif self.payment_released:
            print("Payment has already been released.")
        else:
            self.payment_released = True
            print(f"Payment of {self.payment_amount} released to {self.freelancer}.")

# Crear un contrato inteligente
client = "ClienteA"
freelancer = "FreelancerB"
payment_amount = 1000  # Por simplicidad, utilizamos una cantidad fija

contract = SmartContract(client, freelancer, payment_amount)

# Cliente marca el trabajo como completado
contract.mark_job_done()

# Cliente libera el pago
contract.release_payment()
