from collections import defaultdict

data_list = defaultdict(list)

data_list['apple']= 1
print (data_list)

data_list2 = [1,2,3,4,1,2,3,5]
def_dict = defaultdict(lambda :1)

for number in data_list2:
    def_dict[number] *= number
    
print(def_dict)    

dep = [('sales','john doe'),
('sales','ram sharma'),
('sales','john doe'),
('marketing','shyam sharma'),
('marketing','ram hari'),
]

#### remvoing unique data####
item  = defaultdict(set)
for department,employee in dep:
	item[department].add(employee)
print(item)

### counting the data #### 
total = defaultdict(int)
for department,_ in  dep:
	total['department']+=1
print(total)
