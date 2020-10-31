import pandas as pd


def loan_monthly(month, balance, interest, monthly_pay, months, data):
    payment = 0 if month == 0 else monthly_pay
    paid = round(month*payment, 2)
    data.append({
        "month": month, 
        "balance": balance, 
        "payment": payment, 
        "paid": paid,
        "loan_paid_pct": round(paid / (paid + balance) * 100, 1)
        })
    if month == months:
        return
    else:
        new_balance = (1 + interest) * balance - monthly_pay
        new_balance = round(new_balance, 2)
        if month + 1 == months:
            monthly_pay += new_balance
            new_balance = 0
        loan_monthly(month + 1, new_balance, interest, monthly_pay, months, data)


if __name__ == "__main__":
    """
    Last payment is always greater than the balance in previous month,
    since within the last month the interest is getting accured
    """
    data = []
    debug = not False
    if debug:
        amount, annual_interest, monthly_pay, years = 497, 2.75, 2028.96, 30
    else:
        amount = float(input("Loan in thousands:"))
        annual_interest = float(input("Rate in %:"))
        monthly_pay = float(input("Monthly pay:"))
        years = float(input("Years:"))
        print("-" * 80)
    amount *= 1000
    annual_interest /= 100.

    months = years * 12
    loan_monthly(0, amount, annual_interest / 12., monthly_pay, months, data)
    df = pd.DataFrame(data).set_index('month')
    with pd.option_context('display.max_rows', 24, 'display.max_columns', None):
        print(df[["payment", "balance", "paid", "loan_paid_pct"]].to_csv())
    assert df.shape[0] == months + 1, "something's wrong with the number of payments"
    assert df.loc[months]['balance'] == 0, "final balance is not zero"
