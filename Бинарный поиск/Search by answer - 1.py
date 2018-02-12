import math
w, h, n = map(int, input().split()) # ширина, высота, количество 
area = w * h * n                    # площадь, покрываемая всеми дипломами

def bin_search(area, n, var1, var2):  # разберем 2 случая: 1) сторона доски кратна высоте, 2) кратна ширине
    lo = 0                          
    hi = n                          
    while hi - lo > 1:              
        mid = (lo + hi) // 2        
        if (var1 * mid ) ** 2 < area: # площадь квадратной доски должна быть >= area 
            lo = mid                  # при этом,если сторона квадрата кратна широте, то она должна превосходить высоту
        elif (var1 * mid) ** 2 >= area and var1 * mid  >= math.ceil(n / mid) * var2: # дипломов, выстроенных в вертикальный ряд
            hi = mid                
        else:                         # если мы не можем больше уменьшать диапазон hi - lo
            break
    if var1 * hi >= math.ceil(n / hi) * var2 : # проверяем, выполняется ли условие
        return(var1 * hi)
    else:
        return(h * n)
                                    
ans1 = bin_search(area, n, h, w)                             
ans2 = bin_search(area, n, w, h)
print(min(ans1, ans2))
