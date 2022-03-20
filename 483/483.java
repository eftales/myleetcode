class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> res = new LinkedList<>();

        if(s.length()<p.length()){
            return res;
        }

        int[] cnt = new int[26]; // 统计每个字母出现的次数
        int[] target = new int[26];

        for(int i=0;i<p.length();++i){
            target[p.charAt(i)-'a'] += 1;
            cnt[s.charAt(i)-'a'] += 1;
        }

        if(Arrays.equals(cnt,target)){
            res.add(0);
        }

        for(int i=1;i<=(s.length()-p.length());++i){
            cnt[s.charAt(i-1)-'a'] -= 1;
            cnt[s.charAt(i-1+p.length())-'a'] += 1;
            if(Arrays.equals(cnt,target)){
                res.add(i);
            }

        }


        return res;
    }
}

