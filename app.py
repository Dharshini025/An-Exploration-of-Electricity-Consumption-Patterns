from flask import Flask, render_template

app = Flask(__name__)

TABLEAU_URL = "https://public.tableau.com/views/Electricity_Consumption_Analysis_17840432823280/MonthlyElectricityConsumptionin2019?:embed=true&:showVizHome=no"

@app.route("/")
def dashboard():
    return render_template("dashboard.html", tableau_url=TABLEAU_URL)

if __name__ == "__main__":
    app.run(debug=True)