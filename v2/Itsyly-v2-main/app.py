from flask import Flask, render_template, request


app = Flask(__name__)



attacks = ['Phshing']

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/attacks")
def attacks():
    return render_template('attack.html')

@app.route("/attack/<ack>", methods=["GET"])
def learn(ack):
    urls = {'phishing':['p01.png'],
            'clickjacking':['p06.png','p02.png','p05.png'],
            'ransomware':['p07.png','p08.png','p09.png']}



    if ack=='phishing':
        return render_template('ack.html', ack = ack.upper(), filename = urls['phishing'])
    elif ack =='Clickjacking':
        return render_template('ack.html', ack = ack.upper(), filename = urls['clickjacking'])
    elif ack =='ramsomware':
        return render_template('ack.html', ack = ack.upper(), filename = urls['ransomware'])    


@app.route('/about')
def about():
    return render_template('about.html')




@app.route('/join')
def join():
    return render_template('login.html')



if __name__ == '__main__':
      app.run(debug=True, port=80)