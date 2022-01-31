
class Solution {
    public int maxArea(int[] height) {
        int left=0,right=height.length-1;
        int maxVolume = 0;
        while(left!=right){
            maxVolume = Math.max(maxVolume, (right-left)*Math.min(height[left],height[right]));
            if(height[left]<height[right]){
                left += 1;
            }
            else{
                right -= 1;
            }
        }
        return maxVolume;
    }
}