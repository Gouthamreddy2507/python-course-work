#1.Calculate BMI

def calculate_bmi(weight,height):
  return weight / (height * height)
print('%.2f'%(calculate_bmi(70, 1.75)))
print('%.2f'%(calculate_bmi(90, 1.8)))



def filter_even(numbers):
  res=[]
  for i in numbers:
    if i%2==0:
      res.append(i)
  return res
print(filter_even([1,2,3,4,5,6,7,8]))
print(filter_even([23,45,12,34,89,90,62,74,87]))



def generate_table(n):
  table=[]
  for i in range(1,11):
    table.append(i*n)
  print(table)
generate_table(10)
generate_table(17)
generate_table(12)
generate_table(13)
generate_table(2)



def anagram(str1,str2):
  if len(str1)==len(str2):
    if sorted(str1.lower())==sorted(str2.lower()):
      return True
    else:
      return False
  else:
    return False
print(anagram('Hello','olleh'))
print(anagram('mom','mmm'))
print(anagram('chair','hair'))



def count_words(string):
  feq={}
  for i in string.split():
    if i in feq:
      feq[i]+=1
    else:
      feq[i]=1

  print(feq)
count_words("this is a test this is")
count_words("hello hello world")




'''
[1,2,3,1,2,3,1,2,4,5,3,7]=> 4
[]
[1]
[2,1]
[3,2,1]
[1,3,2]
[2,1,3]
[3,2,1]
[1,3,2]
[2,1,3]
[4,2,1,3]
[5,4,2,1]
[3,5,4,2]
[7,3,5,4]
'''

def lru_cache(request,size):
  cache=[]
  for i in request:
    if i in cache:
      cache.remove(i)
      cache.insert(0,i)
    else:
      if len(cache)<size:
        cache.insert(0,i)
      else:
        cache.pop()
        cache.insert(0,i)
  print(cache)
lru_cache([1,2,3,1,2,3,1,2,4,5,3,7],4)
lru_cache([1,2,3,2,4,1],3)
lru_cache([5,6,7,8],2)
lru_cache([1,2,3,1],2)



def flatten_matrix(matrix):
  flattened=[]
  for i in matrix:
    flattened.extend(i)
  print(flattened)
flatten_matrix([[1, 2], [3, 4]])
flatten_matrix([[5], [6, 7], [8]])



def create_email(first_name, last_name, domain):
  print(f'{first_name.lower()}.{last_name.lower()}@{domain.lower()}.com')
create_email("John", "Doe", "gmail")
create_email("ALICE", "Smith", "yahoo")



def get_factors(n):
  res=[]
  for i in range(1,n+1):
    if n%i==0:
      res.append(i)
  print(res)
get_factors(10)
get_factors(12)
get_factors(16)
get_factors(20)




def format_invoice(item, quantity, price):
  print(f"{item} x{quantity} @ ₹{price} = ₹{quantity*price}")
format_invoice("Pen", 3, 10)
format_invoice("Notebook", 2, 45)