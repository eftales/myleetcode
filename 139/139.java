class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> wordTable = new HashSet<>(wordDict);

        boolean[] canEmbed = new boolean[s.length()+1]; // 默认全为 false
        canEmbed[0] = true;

        for(int i=1;i<s.length()+1;++i){
            for(int j=0;j<=i;++j){
                if(canEmbed[j]==true&&wordTable.contains(s.substring(j,i))){
                    canEmbed[i] = true;
                    break;
                }

            }

        }

        return canEmbed[canEmbed.length-1];
    }
}