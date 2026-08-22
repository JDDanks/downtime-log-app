from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary in-memory storage (we can add a database later)
equipments = ["Conveyor Belt A", "CNC Machine 1"]
downtime_logs = []

@app.route("/")
def dashboard():
    return render_template("index.html", logs=downtime_logs, equipments=equipments)

@app.route("/log-downtime", methods=["GET", "POST"])
def log_downtime():
    if request.method == "POST":
        equipment = request.form.get("equipment")
        reason = request.form.get("reason")
        duration = request.form.get("duration")
        downtime_logs.append({
            "equipment": equipment,
            "reason": reason,
            "duration": duration
        })
        return redirect(url_for("dashboard"))
    return render_template("log_downtime.html", equipments=equipments)

@app.route("/log-equipment", methods=["GET", "POST"])
def log_equipment():
    if request.method == "POST":
        name = request.form.get("equipment_name")
        if name and name not in equipments:
            equipments.append(name)
        return redirect(url_for("dashboard"))
    return render_template("log_equipment.html")

if __name__ == "__main__":
    app.run(debug=True)