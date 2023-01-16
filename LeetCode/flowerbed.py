flowerbed = [0,0,1,0,0]
n = 1
counter = 0

for idx, slot in enumerate(flowerbed):
    if slot == 0:
        if idx == 0:
            if len(flowerbed) == 1:
                counter += 1
            elif len(flowerbed) == 2:
                if flowerbed[idx + 1] == 0:
                    counter += 1
                    flowerbed[idx] = 1
            else:
                if flowerbed[idx + 1] == 0:
                    counter += 1
                    flowerbed[idx] = 1
        elif idx == (len(flowerbed) - 2):
            if flowerbed[idx + 1] == 0 and flowerbed[idx - 1] == 0:
                counter += 1
                flowerbed[idx] = 1
        elif idx == (len(flowerbed) - 1):
            if flowerbed[idx - 1] == 0:
                counter += 1
                flowerbed[idx] = 1
        else:
            if flowerbed[idx + 1] == 0 and flowerbed[idx - 1] == 0:
                counter += 1
                flowerbed[idx] = 1
if counter == n:
    print(True)
