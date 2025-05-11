from assumptions import assumptions
from projections import project_cash_flows
from valuation import discount_cash_flows, calulate_terminal_value

if __name__ == "__main__":
    cash_flows = project_cash_flows(assumptions)
    wacc = assumptions["wacc"]
    terminal_growth = assumptions["terminal_growth"]
    
    #Discounted FCFs

    discounted_cf = discount_cash_flows(cash_flows, wacc)
    
    #Terminal Value

    terminal_value = calulate_terminal_value(cash_flows[-1], wacc, terminal_growth)
    terminal_pv = terminal_value / ((1 + wacc) ** len(cash_flows))

    #Combine to get Enterprise Value

    enterprise_value = sum(discounted_cf) + terminal_pv

    #Convert to Equity Value

    equity_value = enterprise_value - assumptions["net_debt"]
    value_per_share = equity_value / assumptions["shares_outstanding"]

    #print results

    print("Projected Free Cash Flows:")
    for i, fcf in enumerate(cash_flows, 1):
        print(f"Year {i}: ${fcf:,.2f}")


    print("\n--- DCF Valuation Summary ---")
    print(f"Enterprise Value: ${enterprise_value:,.2f}")
    print(f"Equity Value: ${equity_value:,.2f}")
    print(f"Share Price: {value_per_share:,.2f}")