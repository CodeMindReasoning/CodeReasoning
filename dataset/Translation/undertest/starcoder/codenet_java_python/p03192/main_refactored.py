class main:
    import sys
    
    def main():
    	string = sys.stdin.readline().strip()
    	count = 0
    	for i in string:
    		if i == '2':
    			count += 1
    	print(count)
    
    if __name__ == '__main__':
    	main()