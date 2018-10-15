from time import sleep
from threading import Timer

def sleepsort(input):
    sleepsort.result = []
    def add1(x):
        sleepsort.result.append(x)
    mx = input[0]

    for v in input:
        if mx < v: mx = v
        Timer(v, add1, [v]).start()
    sleep(mx+1)
    print(sleepsort.result)

if __name__ == '__main__':
	sleepsort([7, 2 ,100, 1, 9, 45, 2, 33, 7, 77, 25])
	# sleepsort( your array input )

