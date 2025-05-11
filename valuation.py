def discount_cash_flows(cash_flows, wacc):
    discounted = []
    for t, fcf in enumerate(cash_flows, 1):
        pv = fcf / ((1 + wacc) ** t)
        discounted.append(pv)

    return discounted

def calulate_terminal_value(last_fcf, wacc, terminal_growth):
    tv = last_fcf * (1 + terminal_growth) / (wacc - terminal_growth)

    return tv