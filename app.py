
from flask import Flask,render_template,request
from forms import TaxForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "Products"
@app.route('/', methods=['GET','POST'])

def home():
    form=TaxForm()
    f=form.gross_salary.data
    g=0
    d=0
    issizlik=0
    i=0
    y=0
    if request.method=='POST':
        show_block=True
        if form.options.data=='Dövlət və neft sektoru':
            if f<=2500:
                g=((f-200)*14)/100
            else:
                 g=350+(((f-2500)*25)/100)
            d=(f*3)/100
            issizlik=(f*0.5)/100
            if f<=8000:
                i=(f*2)/100
            else:
                i=160+((f-8000)*0.5)/100
            y=f-g-d-issizlik-i
        else:
            if f<=8000:
                g=f*0
                i=(f*2)/100
            else:
                g=(f*14)/100
                i=80+(((f-8000)*0.5)/100)
            if f<=200:
                d=(f*3)/100
            else:
                d=6+(f-200)*0.1
            issizlik=(f*0.5)/100
            y=f-g-d-issizlik-i
    else:
        show_block=False
    
    return render_template("index.html", f=f,g=g,d=d,issizlik=issizlik,y=y,i=i,form=form,show_block=show_block)


if __name__=='__main__':
    app.run(port=5000,debug=True)