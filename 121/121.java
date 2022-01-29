class Solution {
    public int maxProfit(int[] prices) {
        int minVal = prices[0],maxProfit = 0;
        for(int price:prices){
            minVal = Math.min(price,minVal);
            maxProfit = Math.max(maxProfit,price-minVal);
        }
        return maxProfit;
    }
}