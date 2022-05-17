import csv

def main():
  
  conv_weight = round((101*2.205),1)
  conv_height = round((1.75*39.37),1)
  
  ##Code for searching through people list
  with open ('code/people.csv') as csvfile:
    information = csv.DictReader(csvfile, delimiter=',')
    for item in information:
      if item['passenger_gender'] == 'M' and item['weight_in_pounds'] == str(conv_weight) and item['height_in_inches'] == str(conv_height):
        first = item['first_name']
        last = item['last_name']
        nat_id = item['national_id']
        #print(dict(item))
        
        
##Code for searching through rides list      
  with open ('code/rides.csv') as csvfile2:
    rideinfo = csv.DictReader(csvfile2, delimiter=',')
    for ride in rideinfo:
      if ride['start_day'] == '3' and ride['start_month'] == '10' and ride['start_year'] == '2021' and ride['start_hour'] == '0' and ride['start_minute'] == '45':
        bank_conf = ride['bank_confirmation_id']
        #print(dict(ride))
      
      
##Code for searching through transactions
  with open ('code/transactions.csv') as csvfile3:
      transinfo = csv.DictReader(csvfile3, delimiter=',')
      for x in transinfo:
        if x['bank_confirmation_id'] == bank_conf and x['national_id'] == nat_id:
          nat_id = x['national_id']
          #print(dict(x))
    
##Prints all returned information
  print(f"National ID: {nat_id}\nFirst Name: {first}\nLast Name: {last}\n")
    
    
if __name__ == "__main__":
   main()