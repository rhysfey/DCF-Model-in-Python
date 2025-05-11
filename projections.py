def project_cash_flows(assumptions):
    cash_flows = []
    revenue = assumptions["revenue"]

    for year in range(assumptions["forecast_years"]):
        revenue *= (1 + assumptions["revenue_growth"])
        ebit = revenue * assumptions["ebit_margin"]
        nopat = ebit * (1 - assumptions["tax_rate"])
        d_and_a = revenue * assumptions["d_and_a_percent"]
        capex = revenue * assumptions["capex_percent"]
        nwc = revenue * assumptions["nwc_percent"]
        
        fcf = nopat + d_and_a - capex - nwc
        cash_flows.append(fcf)
        
    return cash_flows