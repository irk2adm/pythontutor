# Задача «Часы - 1»
# С начала суток прошло H часов, M минут, S секунд (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60). По данным числам H, M, S определите угол (в градусах), на который повернулаcь часовая стрелка с начала суток и выведите его в виде действительного числа. 

h = int(input())
m = int(input())
s = int(input())
 
print(h * 30 + m * 30 / 60 + s * 30 / 3600)