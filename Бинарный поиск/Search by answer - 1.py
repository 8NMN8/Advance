import math
w, h, n = map(int, input().split()) # ширина, высота, количество 
area = w * h * n                    # площадь, покрываемая всеми дипломами

def bin_search(area, n, var1, var2):  
    lo = -1                         # первый индекс списка   
    hi = n - 1                      # последний индекс + 1
    while hi - lo > 1:              # пока диапазон не сократился до соседних значений 
        mid = (lo + hi) // 2        # выбираем средний индекс из диапазона
        if (var1 * (mid + 1)) ** 2 < area:     # площадь квадратной доски должна быть >= area 
            lo = mid                # при этом,если сторона квадрата кратна широте, то она должна превосходить 
        elif (var1 * (mid + 1)) ** 2 >= area and var1 * (mid + 1) >= math.ceil(n * var1 / (var1 * (mid + 1))) * var2: #высоту дипломов, выстроенных в вертикальный ряд
            hi = mid                
        else:
            break
    if var1 * (hi + 1) >= math.ceil(n * var1 / (var1 * (hi + 1))) * var2 : 
        return(var1 * (hi + 1))
    else:
        return(h * n)
                                    
ans1 = bin_search(area, n, h, w)                             
ans2 = bin_search(area, n, w, h)
print(min(ans1, ans2))
