import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('./app/data.csv')
  country = input('Type Country  => ')
  result = utils.population_by_country(data, country)
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)
    
def world_population_percentage():
  data1 = read_csv.read_csv('./app/data.csv')
  data = list(filter(lambda countries: countries['Continent'] == 'South America',data1 ))

  countries = list(map(lambda data: data['Country/Territory'], data))
  wpp = list(map(lambda data: data['World Population Percentage'], data))
  charts.generate_pie_chart(countries,wpp)
  
  
if __name__ == '__main__':
  world_population_percentage()