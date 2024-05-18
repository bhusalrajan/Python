name = "IBM"
shares = 100
price = 32.2

# print(name,shares,price)
#better one

# print('%10s %10d %10.2f' %(name, shares, price))

# right justify

print('{:>10s} {:>10d} {:>10.2f}'.format(name, shares, price))

#left justify 
print('{:<10s} {:<10d} {:<10.2f}'.format(name, shares, price))