class Solution {

    void mergesort(int[][] intervals,int begin,int end){
        int mid = (begin+end)/2;
        if(end-begin>1){
            mergesort(intervals,begin,mid);
            mergesort(intervals,mid+1,end);
        }
        if(begin>=end){
            return ;
        }
        int[][] res = new int[end-begin+1][];
        int left = begin,right = mid+1,cnt=0;
        while(left<=mid||right<=end){
            if(left>mid||(left<=mid&&right<=end&&intervals[left][0]>intervals[right][0])){
                res[cnt] = intervals[right];
                right += 1;
                cnt += 1;
                continue;
            }

            if(right>end||(left<=mid&&right<=end&&intervals[left][0]<=intervals[right][0])){
                res[cnt] = intervals[left];
                left += 1;
                cnt += 1;
                continue;
            }
        }

        for(int i=begin;i<=end;++i){
            intervals[i] = res[i-begin];
        }

    }
    public int[][] merge(int[][] intervals) {
        mergesort(intervals,0,intervals.length-1);

        List<int[]> resList = new LinkedList<>();
        resList.add(intervals[0]);
        for(int i=1;i<intervals.length;++i){
            if(intervals[i][0]>resList.get(resList.size()-1)[1]){
                resList.add(intervals[i]);
            }
            else{
                resList.get(resList.size()-1)[0] = Math.min(resList.get(resList.size()-1)[0],intervals[i][0]);
                resList.get(resList.size()-1)[1] = Math.max(resList.get(resList.size()-1)[1],intervals[i][1]);
            }
        }

        int[][] res = new int[resList.size()][];
        for(int i=0;i<resList.size();++i){
            res[i] = resList.get(i);
        }

        return res;
    }

    public int[][] mergeSimplify(int[][] intervals){
        Arrays.sort(intervals, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0]-o2[0];
            }
        });
        List<int[]> res = new LinkedList<>();
        res.add(intervals[0]);
        for(int i=1;i<intervals.length;++i){
            if(intervals[i][0]>res.get(res.size()-1)[1]){
                res.add(intervals[i]);
            }
            else{
                res.get(res.size()-1)[0] = Math.min(res.get(res.size()-1)[0],intervals[i][0]);
                res.get(res.size()-1)[1] = Math.max(res.get(res.size()-1)[1],intervals[i][1]);
            }
        }

        return res.toArray(new int[res.size()][]);
    }
}
