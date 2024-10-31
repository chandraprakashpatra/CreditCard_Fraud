import pandas as pd
import random,string

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
cat_id = UniqueIDGenerator()
merch_id = UniqueIDGenerator()

origin = pd.read_csv("credit_card_transactions.csv")

data_category = []
data_merchant = []
data_transactions = []
data_merchant_category=[]

unique_cat = set()
unique_merch = set()
mc_set = set()

category_mapper = {}#name:id 
merchant_mapper = {}
for index,row in origin.iterrows():
    print(index)
    #category table >"
    category_name = row["category"]
    if category_name not in unique_cat:
        category_id = cat_id.generate_random_alphanumeric_id()
        category_mapper[category_name]=category_id
        unique_cat.add(category_name)
        data_category.append({
            "category_id": category_id,
            "category_name": category_name
        })
    else:
        category_id = category_mapper[category_name]
    
    #merchant table>
    name = row["merchant"]
    if name not in unique_merch:
        merchant_id = merch_id.generate_random_alphanumeric_id()
        unique_merch.add(merchant_id)
        merchant_mapper[name]=merchant_id
        data_merchant.append({
            "merchant_id":merchant_id,
            "name":name
        })
    else:
        merchant_id = merchant_mapper[name]
    

    data_transactions.append({
        "trans_num":row["trans_num"],
        "cc_num":row["cc_num"],
        "amount":row["amt"],
        "trans_date_time":row["trans_date_trans_time"],
        "merchant_id":merchant_id,
        "spent_category_id":category_id,
        "fraud":row["is_fraud"]
    })

    #merchant_category table might seem redundant cause the same info is served at Transactions table as well.
    #But the only reason to create this table is for a condition where 
    #a merchant is of a apecific category but have never sold before.(so it have no transaction)
    #So, such a category will not be present in the Transaction table
    check = str(category_id) + str(merchant_id)
    if check not in mc_set:
        data_merchant_category.append({
            "id":index,
            "category_id":category_id,
            "merchant_id":merchant_id
        })
        mc_set.add(check)


Transaction_file = pd.DataFrame(data_transactions)
Category_file = pd.DataFrame(data_category)
Merchant_Category_file = pd.DataFrame(data_merchant_category)
Merchant_file = pd.DataFrame(data_merchant)

Transaction_file.to_csv("Transactions.csv",index=False)
Category_file.to_csv("Category.csv",index = False)
Merchant_file.to_csv("Merchant.csv",index=False)
Merchant_Category_file.to_csv("Merchant_Category.csv",index=False)

print("All 4 tables Created")
