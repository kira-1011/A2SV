if __name__ == '__main__':
    
    def executeCommand(command, list_):
        
        method = command[0]
        params = list(map(int, command[1: ]))
        
        if method == "append":
            list_.append(params[0])
        
        elif method == "insert":
            list_.insert(params[0], params[1])
        
        elif method == "remove":
            list_.remove(params[0])
        
        elif method == "sort":
            list_.sort()
        
        elif method == "pop":
            list_.pop()
        
        elif method == "reverse":
            list_.reverse()
            
        else:
            print(list_)
    
    N = int(input())
    list_ = []
    
    for i in range(N):
        
        command = input().split(" ")
        
        executeCommand(command, list_)
        
        
