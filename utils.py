import pickle 
import json 
import pandas as pd  
import numpy as np 
import warnings
warnings.filterwarnings('ignore')
import config 

class AutoCarPrice():
    
    def __init__(self,normalized_losses,make,fuel_type,
                 aspiration,num_of_doors,body_style,drive_wheels,
                 engine_location,wheel_base,width,
                 engine_type,num_of_cylinders,engine_size,fuel_system,
                 bore,stroke,compression_ratio,horsepower,peak_rpm,
                 city_mpg,highway_mpg):
        
        self.normalized_losses = normalized_losses
        self.fuel_type = fuel_type
        self.aspiration = aspiration
        self.num_of_doors = num_of_doors
        self.drive_wheels = drive_wheels 
        self.engine_location =engine_location
        self.wheel_base = wheel_base
        self.width = width 
        self.num_of_cylinders = num_of_cylinders
        self.engine_size = engine_size
        self.bore = bore
        self.stroke = stroke
        self.compression_ratio = compression_ratio
        self.horsepower = horsepower
        self.peak_rpm = peak_rpm
        self.city_mpg = city_mpg
        self.highway_mpg = highway_mpg 
        
        self.make_col = 'make_' + make
        self.body_style_col = 'body_style_' + body_style
        self.engine_type_col = 'engine_type_'+engine_type
        self.fuel_system_col = 'fuel_system_' +fuel_system
        
    def load_models(self):
        
        with open(config.MODEL_FILE_PATH,'rb') as f :
            self.model = pickle.load(f)
            
        with open(config.JSON_FILE_PATH,'r') as f :
            self.save_data = json.load(f)
            
            self.column_names = np.array(self.save_data['column_names'])
            
    def get_predicted_price(self):
        
        self.load_models()
        
        make_col_index = np.where(self.column_names==self.make_col)[0]
  
        body_style_col_index = np.where(self.column_names==self.body_style_col)[0]
        
        engine_type_col_index = np.where(self.column_names==self.engine_type_col)[0]
        
        fuel_system_col_index = np.where(self.column_names==self.fuel_system_col)[0]
        
        array = np.zeros(len(self.save_data['column_names']))
        
        array[0] = self.normalized_losses
        array[1] = self.save_data['fuel_type'][self.fuel_type]
        array[2] = self.save_data['aspiration'][self.aspiration]
        array[3] = self.save_data['num_of_doors'][self.num_of_doors]
        array[4] = self.save_data['drive_wheels'][self.drive_wheels]
        array[5] = self.save_data['engine_location'][self.engine_location]
        array[6] = self.wheel_base
        array[7] = self.width
        array[8] = self.save_data['num_of_cylinders'][self.num_of_cylinders]
        array[9] = self.engine_size
        array[10] = self.bore
        array[11] = self.stroke
        array[12] = self.compression_ratio
        array[13] = self.horsepower
        array[14] = self.peak_rpm
        array[15] = self.city_mpg
        array[16] = self.highway_mpg

        array[make_col_index] == 1
        array[body_style_col_index] == 1 
        array[engine_type_col_index] == 1
        array[fuel_system_col_index] == 1

        print('Array is :',array)
        
        price = self.model.predict([array])[0]
        
        return price 
    
if __name__ == '__main__':
    
    normalized_losses = 161.00
    fuel_type = 'gas'
    aspiration = 'std'
    num_of_doors = 'two'
    drive_wheels = 'rwd'
    engine_location = 'front'
    wheel_base = 88.60
    width = 64.10
    num_of_cylinders = 'four'
    engine_size = 130.00
    bore = 3.47
    stroke = 2.68
    compression_ratio = 9.00
    horsepower = 111.00
    peak_rpm = 5000.00
    city_mpg = 21.00
    highway_mpg = 27.00

    make = 'alfa_romero'

    body_style = 'convertible'

    engine_type = 'dohc'
            
    fuel_system = '1bbl'


    cars = AutoCarPrice(normalized_losses,make,fuel_type,
                 aspiration,num_of_doors,body_style,drive_wheels,
                 engine_location,wheel_base,width,
                 engine_type,num_of_cylinders,engine_size,fuel_system,
                 bore,stroke,compression_ratio,horsepower,peak_rpm,
                 city_mpg,highway_mpg)
    
    price = cars.get_predicted_price()
    
    print('Price of dream car is $',round(price,2))
    
    
    
      