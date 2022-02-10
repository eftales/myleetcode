class Solution {
    public List<String> generateParenthesis(int n) {
        List<String>[] cache = new ArrayList[n+1];

        List<String> cacheI = new ArrayList<String>();
        cacheI.add("");
        cache[0] = cacheI;

        cacheI = new ArrayList<String>();
        cacheI.add("()");
        cache[1] = cacheI;

        for(int i=2;i<n+1;++i){
            cacheI = new ArrayList<String>();
            for(int li=0;li<=i-1;++li){
                int ri = i-1-li;
                for(String sl: cache[li]){
                    for(String sr:cache[ri]){
                        cacheI.add(sl+"("+sr+")");
                    }
                }
            }
            cache[i] = cacheI;
        }

        return cache[n];

    }
}