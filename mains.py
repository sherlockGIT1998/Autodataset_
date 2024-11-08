from flask import Flask,render_template,request

from utils import AutoCarPrice

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print('Cars Price Prediction....')
    return render_template('index.html')

@app.route('/predict_price',methods=['GET','POST'])
def price_info():
    
    if request.method == 'GET':
        
        print('In GET Method....')
        
        data = request.form
        normalized_losses = eval(data['normalized_losses'])
        make = data['make']
        fuel_type = data['fuel_type']
        aspiration = data['aspiration']
        num_of_doors = data['num_of_doors']
        body_style = data['body_style']
        drive_wheels = data['drive_wheels']
        engine_location = data['engine_location']
        wheel_base = eval(data['wheel_base'])
        width = eval(data['width'])
        engine_type = data['engine_type']
        num_of_cylinders = data['num_of_cylinders']
        engine_size = data['engine_size']
        fuel_system = data['fuel_system']
        bore = eval(data['bore'])
        stroke = eval(data['stroke'])
        compression_ratio = eval(data['compression_ratio'])
        horsepower = eval(data['horsepower'])
        peak_rpm = eval(data['peak_rpm'])
        city_mpg = eval(data['city_mpg'])
        highway_mpg = eval(data['highway_mpg'])
        
        cars = AutoCarPrice(normalized_losses,make,fuel_type,
                 aspiration,num_of_doors,body_style,drive_wheels,
                 engine_location,wheel_base,width,
                 engine_type,num_of_cylinders,engine_size,fuel_system,
                 bore,stroke,compression_ratio,horsepower,peak_rpm,
                 city_mpg,highway_mpg)
        
        price = cars.get_predicted_price()
        
        return f'Price of dream car is $ {round(price,2)}'
    
print('__name__ :',__name__)

if __name__ == '__main__':
    
    app.run()