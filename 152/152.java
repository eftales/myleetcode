class Solution {

    int maxSub(int[] nums,int begin,int end){
        if(end==begin){
            return nums[begin];
        }
        int mCnt = 0;
        List<Integer> subArr = new ArrayList<>();

        int pre = 1;
        for(int i=begin;i<=end;++i){
            if(nums[i]>0){
                pre *= nums[i];
                if(i == end){
                    subArr.add(pre);
                }
            }
            else if(nums[i]<0){
                mCnt += 1;
                subArr.add(pre);
                subArr.add(nums[i]);
                pre = 1;
            }

        }

        if(subArr.size()==0){
            return Integer.MIN_VALUE;

        }

        if(mCnt%2==0){
            // 如果是偶数
            int res = 1;
            for(int elm:subArr){
                res *= elm;
            }
            return res;

        }
        else{
            // 如果是奇数，需要判断不要哪一边

            // 左边的乘积
            int lSub = 1, lIndex=0;
            for(int i=0;i<subArr.size();++i){
                int elm = subArr.get(i);
                lSub *= elm;
                if(elm<0){
                    lIndex = i;
                    break;
                }
            }


            // 右边的乘积
            int rSub = 1,rIndex=0;
            for(int i=subArr.size()-1;i>=0;--i){
                int elm = subArr.get(i);
                rSub *= elm;
                if(elm<0){
                    rIndex = i;
                    break;
                }
            }

            if(mCnt==1){
                // 只有一个负数需要特殊处理
                return Math.max(rSub/subArr.get(rIndex),lSub/subArr.get(lIndex));
            }
            else{

                // 中间的乘积
                int mSub = 1;
                for(int i=lIndex+1;i<rIndex;++i){
                    int elm = subArr.get(i);
                    mSub *= elm;
                }


                return Math.max(mSub*rSub,mSub*lSub);
            }


        }




    }

    public int maxProduct(int[] nums) {
        List<Integer> Index0 = new ArrayList<>();
        for(int i=0;i<nums.length;++i){
            if(nums[i]==0){
                Index0.add(i);
            }
        }

        int pre = -1;
        int maxVal;
        if (Index0.size()==0){
            maxVal = nums[0];
        }
        else{
            maxVal = 0;
        }
        for(int index:Index0){
            maxVal = Math.max(maxVal,maxSub(nums,pre+1,index-1));
            pre = index;
        }
        maxVal = Math.max(maxVal,maxSub(nums,pre+1,nums.length-1));

        return maxVal;
    }
}