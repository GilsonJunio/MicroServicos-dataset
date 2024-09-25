import psycopg
import pandas as pd

# connection = psycopg.connect(
# 	dbname = "laptops",
# 	user = "gilson",
# 	password = "Girusonno_2002",
# 	host = "servidor.czgqkmic2jv4.us-east-2.rds.amazonaws.com",
# 	port = 5432,
# 	)

# cursor = connection.cursor()
# cursor.execute("""CREATE TABLE laptops()""",)


dataset = pd.read_csv("./laptop_prices.csv")

print(dataset)


df = pd.DataFrame(dataset)

for i in df.columns:
	print(i)
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

	# cursor.execute(f"CREATE TABLE laptops({colunas.i} VARCHAR(50))")


	# print(df.columns[i])


# print(colunas)











#cursor.execute("CREATE TABLE laptops" )



# #print(df)
# #print(df.head(12))
# #print(df.dtypes)

# primeiraDuzia = df.iloc[:,0:5]
# print(primeiraDuzia)

# company = df["Company"]
# print(company)

# companyApple = df.loc[df["Company"]=="Apple"]
# print(companyApple)