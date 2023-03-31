from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/masterbarang")
def masterbarang():
    return render_template('masterbarang.html')

@app.route("/mastersupplier")
def mastersupplier():
    return render_template('mastersupplier.html')

@app.route("/masterpelanggan")
def masterpelanggan():
    return render_template('masterpelanggan.html')

@app.route("/formpembelian")
def formpembelian():
    return render_template('formpembelian.html')

@app.route("/datapembelian")
def datapembelian():
    return render_template('datapembelian.html')

@app.route("/formpenjualan")
def formpenjualan():
    return render_template('formpenjualan.html')

@app.route("/datapenjualan")
def datapenjualan():
    return render_template('datapenjualan.html')

# MENIT KE 19.50

# @app.route("/index2")
# def index2():
#     return render_template('index2.html')

# @app.route("/index3")
# def index3():
#     return render_template('index3.html')

if __name__=="__main__":
    app.run(debug = True)