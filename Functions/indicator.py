#buy if avg is greater than rate
#buy is a high count, sell is low count

def indicator(spot_rate,avg):
    count = 0
    if avg > spot_rate:
        count = 1
    elif avg == spot_rate:
        count = 0.5
    else:
        count = 0
    return count