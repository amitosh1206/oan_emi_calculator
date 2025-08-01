# emi_calculator.py

def calculate_emi(principal, annual_rate, tenure_months):
    monthly_rate = annual_rate / (12 * 100)  # Convert to monthly interest rate
    emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure_months) / \
          ((1 + monthly_rate) ** tenure_months - 1)
    return emi


def main():
    print("🔢 Loan EMI Calculator")
    principal = float(input("Enter loan amount (₹): "))
    annual_rate = float(input("Enter annual interest rate (%): "))
    tenure_months = int(input("Enter loan tenure (in months): "))

    emi = calculate_emi(principal, annual_rate, tenure_months)

    print(f"\n✅ Your EMI is: ₹{emi:.2f} per month")

if __name__ == "__main__":
    main()
