from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        ip = str(request.form['ip'])
        ip = ip.split(".")
        new_ip = ''
        for i in ip:
            i = bin(int(i))[2:].zfill(8)
            new_ip += i + "."
        ip = new_ip.rstrip('.')
        page = 1
        return render_template('index.html',ip=ip,page=page)


if __name__ == "__main__":
    app.run(debug=True)