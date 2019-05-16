test = dict()
print(test.items())

print()
test['apple'] = "사과"
test['banana'] = "바나나"
test['sky'] = "하늘"

print(test.items())

data1 = {1:'송아무개',2:'정아무개',3:'김아무개'}

print(data1)
print(data1[1])
print(data1[2])
print(data1[3])

print()
data2 = {"name":"송아무개","age":100,"소속":"kg"}
print(data2)
print(data2["name"])
print(data2["age"])
print(data2["소속"])


print(data2.keys())
print(data2.values())
print(type(data2.keys()))
print(data2.items())

print()
data2["소속"]= "구로점"
print(data2)

singer = {}
singer={"가수이름":"IU","인원수":1,"대표곡":"좋은날","소속사":"로엔"}
print(singer.items())
singer2 = singer

print(singer2)
singer["차트"] = 1
print(singer)
print(singer2)















