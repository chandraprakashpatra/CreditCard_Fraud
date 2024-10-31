import pandas as pd
import string,random

origin = pd.read_csv("credit_card_transactions.csv")

# we will create a Customer.csv file with these columns:
# panID - character(10) and unique : but this is not given need to generate it on the basis of fist+last+dob
# first
# last 
# gender
# job
# dob 
# --------------& CC.csv :
# cc_num - unique PK
# panID 


#uniquely generates a 10 digit number
class UniqueIDGenerator:
    def __init__(self):
        self.generated_ids = set()  # Store unique IDs

    def generate_random_alphanumeric_id(self, length=10):
        characters = string.ascii_letters + string.digits
        
        while True:
            new_id = ''.join(random.choice(characters) for _ in range(length))
            if new_id not in self.generated_ids:
                self.generated_ids.add(new_id)  # Add to the set if unique
                return new_id


#iterating and creating rows for Customer.csv
customer_data = []
cc_data=[]
unique_cc = set()
unique = set()
mapper = {}
id_generator = UniqueIDGenerator()
for index , row in origin.iterrows():
    print(index)
    temp = ''
    first = row['first']
    last = row['last']
    dob = row['dob'] 
    job = row["job"]
    gender = row["gender"]
    temp = first+last+str(dob)
    if temp not in unique:# new Customer (avoiding repititions)
        panid = id_generator.generate_random_alphanumeric_id()#created a new panID
        unique.add(temp)
        mapper[temp]=panid #maps first+last+dob with panid
        customer_data.append({
            'panID':panid,
            'first':first,
            'last':last,
            'gender':gender,
            'dob':dob
        })
    else:#then what is the current panID of the person :
        panid = mapper[temp]
        print("found old customer :",panid,'->',temp)
        #now we we also want to store the panid to ccnum mapping in a separate CC.csv file 

    cc_num = row["cc_num"]
    if cc_num not in unique_cc:#because cc is the PK in CC table
        unique_cc.add(cc_num)
        cc_data.append({
            'cc_num':cc_num,
            'panID':panid
        })



Customer_file = pd.DataFrame(customer_data)
Customer_file.to_csv('Customer.csv',index=False)

CC_file = pd.DataFrame(cc_data)
CC_file.to_csv('CC.csv',index=False)

print("Data saved to CC.csv and Customer.csv")