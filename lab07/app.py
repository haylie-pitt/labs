from flask import Flask, render_template, request
import segno
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    image = None
    message = None
    
    if request.method == 'POST':
        message = request.form['data']
        qr = segno.make(message)
        
        # Store the QR code image in a binary buffer
        buff = io.BytesIO()
        qr.save(buff, kind='svg', scale=3, dark='darkblue', nl=False)
        # Encode the binary image blob to a base64 string
        image = base64.b64encode(buff.getvalue()).decode("utf-8")
    
    return render_template('index.html', image=image, message=message)

if __name__ == '__main__':
    app.run(debug=True)
