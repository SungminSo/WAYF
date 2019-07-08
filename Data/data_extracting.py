import pandas

# df = pandas.read_csv("C:\\Users\\ssm74\\Projects\\WAYF\\data.csv")
# print(df[["ID", "Name", "Photo", "Nationality"]])

col_name = ["ID", "Name", "Photo", "Nationality"]
df = pandas.read_csv("C:\\Users\\ssm74\\Projects\\WAYF\\Data\\data.csv")
extracted_data = df[col_name]
extracted_data.to_csv("C:\\Users\\ssm74\\Projects\\WAYF\\Data\\extracted_data.csv", index=False, na_rep="Nan", encoding="utf-8")

# 국적을 key로 갖고 선수 ID의 리스트를 value로 갖는 딕셔너리
nation_id_dic = {}

# 추출한 데이터를 다시 읽어들여서 확인
extraced = pandas.read_csv("C:\\Users\\ssm74\\Projects\\WAYF\\Data\\extracted_data.csv")
for _, player in test.iterrows():
    # print(player["ID"], player["Nationality"])
    if player["Nationality"] not in nation_id_dic:
        nation_id_dic[player["Nationality"]] = []
    nation_id_dic[player["Nationality"]].append(player["ID"])
    
# 유효한 데이터 재추출
total = 0
valid_nation = []
valid_data = pandas.DataFrame(columns=["ID", "Name", "Photo", "Nationality"])

for nation in nation_id_dic.keys():
    print(nation, len(nation_id_dic[nation]))
    if len(nation_id_dic[nation]) > 20:
        total += 1
        valid_nation.append(nation)

print(len(nation_id_dic.keys()), nation_id_dic.keys())
print(total)
    
count = 0
for _, player in test.iterrows():
    if player["Nationality"] in valid_nation:
        valid_data.loc[count] = [player["ID"], player["Name"], player["Photo"], player["Nationality"]]
        count += 1
            
valid_data.to_csv("C:\\Users\\ssm74\\Projects\\WAYF\\Data\\valid_data.csv", index=False, na_rep="Nan", encoding="utf-8")
