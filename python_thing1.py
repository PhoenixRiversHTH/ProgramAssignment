def triangleArea(base, height):
    area = base*height/2
    print(area)
    return area
    triangleArea(3,6)

m = 5
n = 5
areaList = []
i = 0
for b in range(0,n):
    for h in range(0,m):
        areaList.append(triangleArea(b,h))
    
print (areaList)