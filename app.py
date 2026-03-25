from flask import Flask, render_template, request
from converter import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        value = request.form["value"].strip()
        conversion_type = request.form["type"]

        if not value:
            error = "Please enter a value"
        else:
            try:
                if conversion_type == "dec_to_bin":
                    result = decimal_to_binary(int(value))

                elif conversion_type == "bin_to_dec":
                    result = binary_to_decimal(value)
                    if result is None:
                        error = "Invalid binary number"

                elif conversion_type == "dec_to_hex":
                    result = decimal_to_hex(int(value))

                elif conversion_type == "hex_to_dec":
                    result = hex_to_decimal(value)
                    if result is None:
                        error = "Invalid hexadecimal number"

                elif conversion_type == "bin_to_hex":
                    result = binary_to_hex(value)
                    if result is None:
                        error = "Invalid binary number"

                elif conversion_type == "hex_to_bin":
                    result = hex_to_binary(value)
                    if result is None:
                        error = "Invalid hexadecimal number"

            except:
                error = "Enter a valid number"

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)