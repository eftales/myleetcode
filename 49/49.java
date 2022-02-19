class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> counter = new HashMap<String,List<String>>();
        for(String str:strs){
            char[] array = str.toCharArray();
            Arrays.sort(array);
            String key = new String(array);
            if(counter.containsKey(key)){
                counter.get(key).add(str);
            }
            else{
                List<String> value = new LinkedList<>();
                value.add(str);
                counter.put(key, value);
            }

        }
        return new ArrayList<List<String>>(counter.values());
    }
}
