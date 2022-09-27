class MedianFinder {
private:
    vector<int> minHeap;
    vector<int> maxHeap;
    int totalLength;
    
public:
    MedianFinder() {
        vector<int> minHeap;
        vector<int> maxHeap;
        
        this -> totalLength = 0;
        
        this -> minHeap = minHeap;
        
        make_heap(this -> minHeap.begin(), this -> minHeap.end(), greater<>());
        
         this -> maxHeap = maxHeap;
        
        make_heap(this -> maxHeap.begin(), this -> maxHeap.end());
    }
    
    void addNum(int num) {    
        
        maxHeap.push_back(num);
        push_heap(maxHeap.begin(), maxHeap.end());
        totalLength++;
        
        int n = maxHeap.size();
        
        int maxFront = maxHeap.front();
        
        if(n != (totalLength / 2))
        {
            pop_heap(maxHeap.begin(), maxHeap.end());
            
            maxHeap.pop_back();
            
            minHeap.push_back(maxFront);
            
            push_heap(minHeap.begin(), minHeap.end(), greater<>());
        }
        
        maxFront = maxHeap.front();
        
        int minFront = minHeap.front();
        
        if(!maxHeap.empty() && maxFront > minFront)
        {   
            pop_heap(maxHeap.begin(), maxHeap.end());
            
            maxHeap.pop_back();

            pop_heap(minHeap.begin(), minHeap.end(), greater<>());
            
            minHeap.pop_back();
            
            maxHeap.push_back(minFront);
            
            push_heap(maxHeap.begin(), maxHeap.end());
            
            minHeap.push_back(maxFront);
            
            push_heap(minHeap.begin(), minHeap.end(), greater<>());   
        }
    }
    
    double findMedian() {
        
        int n = maxHeap.size(), m = minHeap.size();
        
        double median = 0;
        
        if(n == m)
            median = double(maxHeap.front() + minHeap.front()) / 2;

        else
             median = minHeap.front();
        
        return median;
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */