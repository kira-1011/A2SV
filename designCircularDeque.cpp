class MyCircularDeque {
private:
    vector<int> CircularDeque;
    
    int noElements = 0;
    
    int k;
    
    int front = -1;
    
    int rear = -1;
    
   
    
public:
    MyCircularDeque(int k) {
        
        vector<int> CircularDeque (k, -1);
        
        this -> CircularDeque =  CircularDeque;
        
        this -> k = k;
    }
    
    bool insertFront(int value) {
        
         if(isEmpty())
        {
            front++;
            rear++;
            CircularDeque[front] = value;
            noElements++;
            return true;
        }
        
        if(!isFull())
        {
            front = (--front) % k;
            
            if(front < 0)
                front = k - 1;
            
            while(CircularDeque[front] != -1)
                 front = (--front) % k;
            
            CircularDeque[front] = value;
            
            noElements++;
            
            return true;
        }
        return false;
    }
    
    bool insertLast(int value) {
         cout << "executing" << endl;
        if(isEmpty())
        {
            rear++;
            CircularDeque[rear] = value;
            front++;
            noElements++;
            return true;
        }
            
        if(!isFull())
        {
            rear = (++rear) % k;
            
            while(CircularDeque[rear] != -1)
               rear = (++rear) % k;
            
            CircularDeque[rear] = value;
            noElements++;
            
            return true;
        }
        
        return false;
        
    }
    
    bool deleteFront() {
        
        cout << "executing" << endl;
        if(!isEmpty())
        {
            CircularDeque[front] = -1;
            
            noElements--;
            
            if(isEmpty())
            {
                front = -1;
                rear = -1;
                return true;
            }
            
            front = (++front) % k;
            
            while(CircularDeque[front] == -1)
                front = (++front) % k;
            
            return true;
        }
        
        return false;
        
    }
    
    bool deleteLast() {
        cout << "executing" << endl;
        if(!isEmpty())
        {
            CircularDeque[rear] = -1;
            
            noElements--;
            
            if(isEmpty())
            {
                front = -1;
                rear = -1;
                return true;
            }
            
            rear = (--rear) % k;
            
            if(rear < 0)
                rear = k - 1;
            
            while(CircularDeque[rear] == -1)
                rear = (--rear) % k;
            
            return true;
        }
        
        return false;
    }
    
    int getFront() {
        cout << "executing" << endl;
        if(isEmpty())
            return -1;
        
        return CircularDeque[front];
        
    }
    
    int getRear() {
        cout << "executing" << endl;
        if(isEmpty())
            return -1;
        
        return CircularDeque[rear];
    }
    
    bool isEmpty() {
        return (noElements == 0);
    }
    
    bool isFull() {
        return (noElements ==  k);
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */