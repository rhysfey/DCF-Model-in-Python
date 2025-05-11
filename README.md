DCF Valuation Tool

Tech stack 
	Language = Python
	Libraries = pandas, numpy, matplotlib oe plotly, streamlit (gui)
	Extras = Modular design (OOP/function), unit tests, CLI and/or web interface. CSV inport/export
	
Features
	Input assumptions:
		Revenur growth
		EBIT Margin
		Tax Rate 
		CapEx, D&A, NWC
		WACC
		Terminal growth rate or exit multiple
		
	Projection Engine
		5-10 year forward financials
		Free cash flow calculation
		
	Discounting
		Presebt value of projected cash flow
		Terminal value
		Enterprise Value & Equity Value
		
	Outputs
		Value per share
		Sensitivity Analysis (WACC vs Terminal growth)
		Plots: FCF, EV over time
		
Stretch Goals
	Pull data from yaho or somewhere
	Export PDF valuation summary
	Web UI with Streamlit or flask
	Monte carlo simulations for certainity