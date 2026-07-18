from flask import Flask, render_template_string

app = Flask(__name__)
TABLEAU_URL = "https://public.tableau.com/views/Electricity_Consumption_Analysis_17840432823280/MonthlyElectricityConsumptionin2019?:embed=true&:showVizHome=no"

PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Electricity Consumption Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin: 0; padding: 20px; }
        .tableau-container { display: flex; justify-content: center; padding: 20px; }
        iframe { border: none; max-width: 100%; }
    </style>
</head>
<body>
    <h1>India Electricity Consumption Analysis</h1>
    <div class="tableau-container">
        <iframe src="{{ tableau_url }}" width="1200" height="800" frameborder="0" allowfullscreen></iframe>
    </div>
</body>
</html>
"""

@app.route("/")
def dashboard():
    return render_template_string(PAGE, tableau_url=TABLEAU_URL)

if __name__ == "__main__":
    app.run(debug=True)