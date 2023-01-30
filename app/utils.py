def get_population(country_dict): 
  years = ['2022', '2020', '2015', '2010', '2000','1990','1980', '1970']
  population_dict = {year:int(country_dict[year + ' Population']) for year in years}
  return population_dict.keys(),population_dict.values()
  

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result