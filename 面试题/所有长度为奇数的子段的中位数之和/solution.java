/**
给出长度为n的数组，求所有长度为奇数的子段的中位数之和

e.g.: 

原数组 [2,3,1,4]
长度为奇数的子段有： [2],[3],[1],[4],[2,3,1],[3,1,4]
中位数有：           2   3   1   4     2       3
和为： 15

要求算法复杂度为 n*n*logn

可以参考 leetcode 295

*/

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


class Solution{

    public void midSum(int[] nums){
        int res = 0;
        for(int i=0;i<nums.length;++i){
            MedianFinder medianFinder = new MedianFinder();
            int begin = i;
            medianFinder.addNum(nums[i]);
            res += medianFinder.findMedian();

            for(int gap=3;(i+gap)<=nums.length;gap+=2){
                for(int j=0;j<2;++j){
                    medianFinder.addNum(nums[begin+1+j]);
                }
                begin += 2;

                res += medianFinder.findMedian();

            }
        }

    }


}




