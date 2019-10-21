import pandas as pd


def loan_monthly(payment, balance, interest, monthly_pay, months, data):
    if payment == 0:
        payment_paid = 0
    else:
        payment_paid = monthly_pay
    data.append({"month": payment, "balance": balance, "payment": payment_paid})
    if payment == months:
        return
    else:
        new_balance = (1 + interest) * balance - monthly_pay
        new_balance = round(new_balance, 2)
        if payment + 1 == months:
            monthly_pay += new_balance
            new_balance = 0
        loan_monthly(payment + 1, new_balance, interest, monthly_pay, months, data)


if __name__ == "__main__":
    """
    Last payment is always greater than the balance in previous month,
    since within the last month the interest is getting accured
    """
    data = []
    amount, annual_interest, monthly_pay, years = 750000, 0.0373, 3464.86, 30
    # amount, annual_interest, monthly_pay, years = 150000, 0.06, 899.33, 30
    # amount, annual_interest, monthly_pay, years = 2000, 0.09, 91.37, 2
    months = years * 12
    loan_monthly(0, amount, annual_interest / 12., monthly_pay, months, data)
    df = pd.DataFrame(data).set_index('month')
    with pd.option_context('display.max_rows', 24, 'display.max_columns', None):
        print(df[["payment", "balance"]])
    assert df.shape[0] == months + 1, "something's wrong with the number of payments"
    assert df.loc[months]['balance'] == 0, "final balance is not zero"
