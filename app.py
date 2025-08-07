from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('laptop_model.lb')  # replace with your model filename

history = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/project', methods=['GET', 'POST'])
def project():
    if request.method == 'POST':
        # Extract input fields
        brand = int(request.form['brand'])
        processor_brand = int(request.form['processor_brand'])
        processor = int(request.form['processor'])
        gen = int(request.form['gen'])
        ram = int(request.form['ram'])
        ssd = int(request.form['ssd'])
        hdd = int(request.form['hdd'])
        os = int(request.form['os'])
        os_bit = int(request.form['os_bit'])
        gpu = int(request.form['gpu'])
        warranty = int(request.form['warranty'])
        touchscreen = int(request.form['touchscreen'])
        msoffice = int(request.form['msoffice'])
        rating = float(request.form['rating'])
        num_ratings = int(request.form['num_ratings'])
        num_reviews = int(request.form['num_reviews'])

        print('output>>>>>>',brand, processor_brand, processor, gen, ram, ssd, hdd, os, os_bit,
                       gpu, warranty, touchscreen, msoffice, rating, num_ratings, num_reviews)
        
        input_data = [[brand, processor_brand, processor, gen, ram, ssd, hdd, os, os_bit,
                       gpu, warranty, touchscreen, msoffice, rating, num_ratings, num_reviews]]
        
        prediction = model.predict(input_data)[0]
        history.append((brand, processor_brand, processor, gen, ram, ssd, hdd, os, os_bit,
                        gpu, warranty, touchscreen, msoffice, rating, num_ratings, num_reviews, prediction))
        
        prediction = prediction.item()
        prediction = round(prediction,2)
        print("Prediction from model:", prediction)
        return render_template('project.html', prediction=prediction)

    return render_template('project.html')

@app.route('/history')
def show_history():
    return render_template('history.html', history=history)

if __name__ == '__main__':
    app.run(debug=True)
