import pandas as pd


def loan_montly(payment, balance, interest, monthly_pay, months, data):
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
        loan_montly(payment + 1, new_balance, interest, monthly_pay, months, data)


if __name__ == "__main__":
    data = []
    amount, interest, monthly_pay, years = 150000, 0.06, 899.33, 30
    # amount, interest, monthly_pay, years = 2000, 0.09, 91.37, 2
    months = years * 12
    loan_montly(0, amount, interest/12., monthly_pay, months, data)
    df = pd.DataFrame(data).set_index('month')
    print(df[["payment", "balance"]])
    assert df.shape[0] == months + 1, "something's wrong with the number of payments"
    assert df.loc[months]['balance'] == 0, "final balance is not zero"
