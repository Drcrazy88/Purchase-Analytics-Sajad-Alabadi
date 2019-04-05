        
import csv
from collections import defaultdict

columns = defaultdict(list) # each value in each column is appended to a list
with open('./input/products.csv',mode='r',encoding="utf8") as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v)
            # append the value into the appropriate list
                                 # based on column name k
                                 
                                 # Creating list of Product Id and Department Id
Product_Id=(columns['product_id'])
DepartmentId=(columns['department_id'])
Department_Int=[(int(x)) for x in DepartmentId] # Change the Department Id to Int
Product_Idv=list(zip(DepartmentId, Product_Id)) # merge the 2 lists togather
Product_Idv_zZz = [(int(x), int(y)) for x, y in Product_Idv] # chane the merged list to int
list_of_lists_Product_Idv= [list(elem) for elem in Product_Idv_zZz ] # Make the tuples lists as lists of lists 

sum(map(lambda x: x.pop(0), list_of_lists_Product_Idv)) # remove the first Columns 

flat_list_Idv = [] 
for sublist in list_of_lists_Product_Idv: # make the one deminsional array flat      
    for item in sublist:
        flat_list_Idv.append(item)
  

EachDepartTotallOrder=dict((i, DepartmentId.count(i)) for i in DepartmentId) # Count the Number  of Orders in each Department Indv
EachDepartTotallOrderList=list(EachDepartTotallOrder.items()) #Convert The Dict TO a List 
EachDepartTotallOrderLisofflist = [list(elem) for elem in EachDepartTotallOrderList] # Convert the Tuples in the List to list so can its can be modified 
zZzSorted = [(int(x), int(y)) for x, y in EachDepartTotallOrderLisofflist ] # Convert the  lists of lists to Int Values 

SortedFinalDepartment=sorted(zZzSorted , key = lambda x: (x[0], x[1])) # Sort the department Orders 
SortedFinalDepartmentListofList = [list(elem) for elem in SortedFinalDepartment] # Convert the tuples to lists 
SortedFinalDepartmentListofList2 = [list(elem) for elem in SortedFinalDepartment] # Convert the tuples to lists 

# divide the the 2 elements in the lists of list to one list of lists each to create flat 


Number_of_Department_Final=SortedFinalDepartmentListofList #remove the orders_id Columns
sum(map(lambda x: x.pop(1), Number_of_Department_Final))

Flat_Number_of_Department_Final=[]  #create new falt list of Department Num

for sublist in Number_of_Department_Final:
    for item in sublist:
        Flat_Number_of_Department_Final.append(item)
        
Flat_Number_of_Department_Final_2=[]  #create new falt list of Department Num

for sublist in Number_of_Department_Final:
    for item in sublist:
        Flat_Number_of_Department_Final_2.append(item)


Number_of_Total_Orders_In_Department=SortedFinalDepartmentListofList2 #remove the Departments_id Columns
sum(map(lambda x: x.pop(0), Number_of_Total_Orders_In_Department))
Flat_Number_of_Total_Orders_In_Department_final=[]
for sublist in Number_of_Total_Orders_In_Department:
    for item in sublist:
        Flat_Number_of_Total_Orders_In_Department_final.append(item)


########################################################################################
        ##################################################################
        #################################################################
           ##########################################################
                    ######################################
                    ######################################

 # Stage 2 importing the Order_Products file                            
                                 
columns1 = defaultdict(list) # each value in each column is appended to a list
                                 
with open('./input/order_products.csv',mode='r',encoding="utf8") as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (kk,vv) in row.items(): # go over each column name and value 
            columns1[kk].append(vv)
            # append the value into the appropriate list
                                 # based on column name k                    
                             

ProductId_2=(columns1['product_id']) # make a columns with Product Id
reoreded= (columns1['reordered'])  # Make a colums with Reordered as zero treat first Orders 


ListOfReordered=list(zip(ProductId_2, reoreded)) # making alist with three along with department id

zZz = [(int(x), int(y)) for x, y in ListOfReordered]

list_of_lists_forReoredered = [list(elem) for elem in zZz ] #Converting the Tuple into List #Converting the Tuple into List

 # Converting the list into Int so we can loop over them

FirstOrder=[] #making new list of the new items ordered for the frist time for each department
for r in list_of_lists_forReoredered:
    #rr=list(r)
    
    if r[1]==0:
        FirstOrder.append(r)
                      
        print('first time ordered')

list_of_lists_forReoredered = [list(elem) for elem in FirstOrder]  # covert the tuples to lists
FirsrOrderFil2=sum(map(lambda x: x.pop(1), list_of_lists_forReoredered))

flat_list = []
for sublist in list_of_lists_forReoredered: # make the one deminsional array flat      
    for item in sublist:
        flat_list.append(item)

flat_list_Idv.extend(flat_list)
countvscount=dict((i, flat_list_Idv .count(i)) for i in flat_list_Idv )
countvscountList=list(countvscount.items())
countvscountListoflist = [list(elem) for elem in countvscountList]
FirsrOrderFil3=sum(map(lambda x: x.pop(0), countvscountListoflist))
FirstOrder_Flat = []
for sublist in countvscountListoflist: # make the one deminsional array flat      
    for item in sublist:
        FirstOrder_Flat.append(item)
 
FirstOrderFinal = [x-1 for x in FirstOrder_Flat]  # getting the first order flags 
       
  
#-----------------------------------------------------------------------
 
# Makeing  one list of the deparment Id and First Order Flags
DepartmentandFirstOrder = [(Department_Int[i], FirstOrderFinal[i]) for i in range(0, len(Department_Int))] 
DepartmentandFirstOrder_list=[list(elem) for elem in DepartmentandFirstOrder]


Firsr_order_list=[] #making new list of the new items ordered for the frist time for each department
for s in DepartmentandFirstOrder_list:
    #rr=list(r)
    

    if s[1]==1:
        Firsr_order_list.append(s)
       
        
FirsrOrderFil3=sum(map(lambda x: x.pop(1), Firsr_order_list)) # remove the second column

flat_list_First_order = [] 
for sublist in Firsr_order_list: # make the one deminsional array flat      
    for item in sublist:
        flat_list_First_order.append(item)

flat_list_First_order_count=list((i, flat_list_First_order.count(i)) for i in flat_list_First_order ) # counting the first order in each department 
First_Order_count_List_of_List=[list(elem) for elem in flat_list_First_order_count] # changing them to a list

First_Order_count_List_of_Listr_Str = [(str(x), str(y)) for x, y in First_Order_count_List_of_List] # fisrt order count converted to str
            
xxx = len(Flat_Number_of_Department_Final)  # geting the lenght of department number to create array of zeros          
           
arrrrrrr = [0 for _ in range(xxx)]   # creating array of zeros            
    
         
xxx_arrr=[(Flat_Number_of_Department_Final[i], arrrrrrr [i]) for i in range(0, len(Flat_Number_of_Department_Final))] # merging the number of department id with the zero array           
xxx_arrr_listoflist = [list(elem) for elem in xxx_arrr] # creating list of above list
zZz_str = [(str(x), str(y)) for x, y in xxx_arrr_listoflist] # converting the list to str
list_of_lists_of_lists = [list(elem) for elem in zZz_str ] # converting the above to list of lists 
    
# Passing the number of the first order to the department Ids

for iii in list_of_lists_of_lists:
     for j in First_Order_count_List_of_Listr_Str:
        if j[0] == iii[0]:
            for item in list_of_lists_of_lists:
                if item[1]=='0' and item[0]==iii[0]:
                    item[1] = j[1]

                  
list_of_lists_of_lists_int = [[int(float(jjjj)) for jjjj in iiiiii] for iiiiii in list_of_lists_of_lists] # converting the list to int
sum(map(lambda x: x.pop(0), list_of_lists_of_lists_int)) # removing index 0 from the list of lists     
#------------------------------------------------------------------------                    
                     
FinalWithoutRatio=[[x, y, z] for x, y, z in zip(Number_of_Department_Final, Number_of_Total_Orders_In_Department, list_of_lists_of_lists_int)] #making one list of Department Id and Orders Number and first orders Numbers 

FinalWithoutRatio_ListOfList = [list(elem) for elem in FinalWithoutRatio] #convert the tuples to lists so its can be modified

flat_list_of_lists_of_lists_int= []
for sublist in list_of_lists_of_lists_int: # make the one deminsional array flat      
    for item in sublist:
        flat_list_of_lists_of_lists_int.append(item)




res = [iiiiiii / jjjjj for iiiiiii, jjjjj in zip(flat_list_of_lists_of_lists_int,Flat_Number_of_Total_Orders_In_Department_final)] # find the Ratios

ResNew2= [format(x, '.2f') for x in res] # make the ratios dec.


Final_Without_No_Orders_Checking = [(Flat_Number_of_Department_Final[i], Flat_Number_of_Total_Orders_In_Department_final[i],flat_list_of_lists_of_lists_int[i],ResNew2[i]) for i in range(0, len(Flat_Number_of_Department_Final))] # Making the final List

FinalListCompleted=[] # Filter Department with zero Orders 
for rr in Final_Without_No_Orders_Checking:
        
    if rr[1]!=0:
        FinalListCompleted.append(rr)
    
# export the file to csv
with open('./output/report.csv','w', newline='') as f: # Save the files with the main folder
    writer = csv.writer(f)
    writer.writerow(['department_id','number_of_orders','number_of_first_orders','percentage'])
    writer.writerows(FinalListCompleted)
                    
   
