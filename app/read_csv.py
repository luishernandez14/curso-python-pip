import csv 

def read_csv(path):
  country_info = []
  with open(path,'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader)
    for row in reader:
      data_dict = {header:row for (header,row) in zip(header,row)}
      country_info.append(data_dict)
  return country_info
      
if __name__ == '__main__': 
  data = read_csv('./app/data.csv') 
  print(data[0])