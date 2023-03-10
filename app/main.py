import utils
import read_csv
import charts
import pandas as pd

def run():

  #USING PANDAS

  df = pd.read_csv('data.csv') #Reading a csv
  df = df[df['Continent'] == 'Europe'] #Filtering Coutries by continent

  countries = df['Country/Territory'].values
  wpp = df['World Population Percentage'].values
  


  
  #USING CSV 

  data = read_csv.read_csv('./data.csv')
  country = input('Type Country  => ')
  result = utils.population_by_country(data, country)
  if len(result) > 0:
    country_data = result[0]
    labels, values = utils.get_population(country_data)
    charts.generate_bar_chart(country, labels, values)

  '''  
  data1 = list(filter(lambda countries: countries['Continent'] == 'Asia',data ))

  countries = list(map(lambda data: data['Country/Territory'], data1))
  wpp = list(map(lambda data: data['World Population Percentage'], data1))
  '''
  charts.generate_pie_chart(countries,wpp)
    
  
if __name__ == '__main__':
  run()