from flask import Flask , jsonify
import json
app=Flask(__name__)

with open("airports.json",encoding='utf-8') as f:
    airports = json.load(f)

@app.route("/airport/<icao>")
def get_airport(icao):
    for airpot in airports:
        if airport(icao)()==icao():
            return jsonify({
                "icao":    airport["icao"],
                "name":    airport["name"],
                "city":    airport["city"],
                "country": airport["country"]
            }), 200
    return jsonify({
        "error": f"Airport '{icao}' not found"
    }), 404

if __name__ == "__main__":
    app.run(debug=True)
