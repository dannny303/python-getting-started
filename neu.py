from flask import Flask, render_template, url_for, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def neupage():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def servicelist():
    return render_template('services.html')

@app.route('/contact')
def contactform():
    return render_template('contact.html')

@app.route('/portfolio')
def photo():
    return render_template('photo-portfolio.html')

@app.route('/mallproject')
def mall():
    return render_template('mall-improve-portfolio.html')

@app.route('/portfolio')
def neuphoto():
    return render_template('photo-portfolio.html')

@app.route('/portfolio2')
def neuphoto2():
    return render_template('photo-portfolio-2.html')

@app.route('/portfolio3')
def neuphoto3():
    return render_template('photo-portfolio-3.html')

@app.route('/projects')
def neuprojects():
    return render_template('project-portfolio.html')

@app.route('/timeline')
def photime():
    return render_template('photimeline.html')

@app.route('/retail')
def retailprice():
    return render_template('retail.html')

@app.route('/otherservice')
def other():
    return render_template('otherservice.html')

@app.route('/docks')
def loadingdocks():
    return render_template('docks.html')

@app.route('/condodocs')
def hoadocs():
    return render_template('condodocs.html')

@app.route('/entrysys')
def entrysystem():
    return render_template('entrysys.html')

@app.route('/laundry')
def laundry():
    return render_template('laundry.html')

@app.route('/mail')
def mail():
    return render_template('mail.html')

@app.route('/trash')
def trash():
    return render_template('trash.html')

@app.route('/internetdirectv')
def internetandcable():
    return render_template('netandcable.html')

if __name__ == '__main__':
    app.run()
