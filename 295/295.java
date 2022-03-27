class MedianFinder {
    Queue<Integer> queBiggerMin; // 大于，最小堆
    Queue<Integer> queSmallerMax; // 小于等于，最大堆
    public MedianFinder() {
        queBiggerMin = new PriorityQueue<>((a,b)->(a-b));
        queSmallerMax = new PriorityQueue<>((a,b)->(b-a));
    }

    public void addNum(int num) {
        if(queSmallerMax.size()==0||num<=queSmallerMax.peek()){
            // 无元素 或 小于 中位数，应该插入到 queSmallerMax 中
            queSmallerMax.add(num);
            if(queSmallerMax.size()>(queBiggerMin.size()+1)){
                // 但是 queSmallerMax 的长度有点超了
                // 将 queSmallerMax 中最大的元素移动到 queBiggerMin 中
                queBiggerMin.add(queSmallerMax.poll());
            }
        }
        else{
            // 大于 中位数，应该插入到 queBiggerMin 中
            queBiggerMin.add(num);
            if(queSmallerMax.size()<queBiggerMin.size()){
                // 但是 queBiggerMin 的长度有点超了
                // 将 queBiggerMin 中最小的元素移动到 queSmallerMax 中

                queSmallerMax.add(queBiggerMin.poll());
            }

        }
    }

    public double findMedian() {
        if(queSmallerMax.size()==queBiggerMin.size()){
            return (queSmallerMax.peek()+queBiggerMin.peek())/2.0;
        }
        else{
            return queSmallerMax.peek();
        }


    }
}
