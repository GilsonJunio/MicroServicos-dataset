import requests
import pandas as pd
import psycopg
addressRDS = 'servidor.czgqkmic2jv4.us-east-2.rds.amazonaws.com'
addressAPI = 'https://20lqmafpv6.execute-api.us-east-2.amazonaws.com/default/bancodedados'
#print(connection)
auth_akID = ''
auth_secretAK =''

dataset = pd.read_csv("./laptop_prices.csv")
# print(dataset)

# print("\n/-######### - DATAFRAME -#########-/")

df = pd.DataFrame(dataset)
# print(df)

# print("\n/-######### - COMPANY COLUMN -#########-/")


# colunas = df["Company"]
# print(colunas)

# print("\n/-######### - APPLE COLUMNS -#########-/")

# colunasDaApple = df["Company"] == "Apple"
# print(colunasDaApple)

# print("\n/-######### - APPLE ROWS -#########-/")
# address = 'https://339aigmes2.execute-api.us-east-2.amazonaws.com/default/meuteste'

# apple = df[df["Company"]=="Apple"]
# print(apple) 
# print(apple.dtypes) 

# for i in apple:
# 	variavel = i
# 	print(variavel) 
# 	# post = requests.post(address,coluna={})




# print("--------------------------")

#Puxar dados pela API#
get = requests(addressAPI,user=auth_akID+":"+auth_secretAK)
print(get)
print(get.text)



#Enviar dados para API#

# get = requests.get('https://1agu4qhsa5.execute-api.us-east-2.amazonaws.com/default/primeirafuncao')
# print(get)
# print(get.text)

# post = requests.post('https://1agu4qhsa5.execute-api.us-east-2.amazonaws.com/default/primeirafuncao',data={"coluna":"valor"})
# print(post)
# print(post.text)


















#Criar Linhas pela API

# post = requests.post('https://339aigmes2.execute-api.us-east-2.amazonaws.com/default/meuteste')
# print(post)
# print(post.text)

# appleRows = postColunas.text
# appleRows








# colunasDaApple = df.loc[df["Company"]=="Apple"]
# print(colunasDaApple)

# for i in df.columns:
# 	print(i)
	
#print(df)
# print(df.head(12))
# #print(df.tail(12))
# print(df.columns[0])

# colunas = df.columns

# print(colunas)
# print(df)

# colunas = df.columns.astype('object')



	# colunas = {i:i}

	# print(colunas)


	# print(df.columns[i])


# print(colunas)

# #print(df)
# #print(df.head(12))
# #print(df.dtypes)

# primeiraDuzia = df.iloc[:,0:5]
# print(primeiraDuzia)

# company = df["Company"]
# print(company)

# companyApple = df.loc[df["Company"]=="Apple"]
# print(companyApple)
