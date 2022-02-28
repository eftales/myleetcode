class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> s = new Stack<>();
        int[] ans = new int[temperatures.length];

        for(int ind=0;ind<temperatures.length;++ind){
            while(!s.empty() && temperatures[s.peek()]<temperatures[ind]){
                ans[s.peek()] = ind - s.peek();
                s.pop();
            }
            s.push(ind);
        }

        // 不需要加这一行，默认值本来就是 0
//        while(!s.empty()){
//            ans[s.pop()] = 0;
//        }

        return ans;
    }
}
