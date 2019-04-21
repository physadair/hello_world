public class FindMedianSortedArrays
{
    public static double findMedianSortedArrays(int[] nums1, int[] nums2) 
    {
        if (nums1.length > nums2.length) {
            int[] tmp = nums1;
            nums1 = nums2;
            nums2 = tmp;
        }

        int max_of_left = 0, min_of_right = 0;
        int m = nums1.length, n = nums2.length;
        int i = m/2, j;
        while (true) {
            j = (m + n)/2 - i;
            if (i<m && nums1[i]<nums2[j-1]) 
                i += 1;
            else if (i>0 && nums2[j]<nums1[i-1])
                i -= 1;
            else {
                if (i==m) min_of_right = nums2[j];
                else if (j==n) min_of_right = nums1[i];
                else min_of_right = Math.min(nums1[i], nums2[j]);

                if ((m+n)%2==1)
                    return min_of_right;

                if (i==0) max_of_left = nums2[j-1];
                else if (j==0) max_of_left = nums1[i-1];
                else max_of_left = Math.max(nums1[i-1], nums2[j-1]);

                return (max_of_left+min_of_right)/2.;

            }
        }
    }
    
    public static int getKth(int[] nums1, int[] nums2, int k)
    {
        if (nums1.length > nums2.length) 
            return getKth(nums2, nums1, k);

        if (nums1.length == 0) 
            return nums2[k-1];

        if (k == 1)
            return Math.min(nums1[0], nums2[0]);

        int i = Math.min(nums1.length, k/2);
        int j = Math.min(nums2.length, k/2);
        if (nums1[i-1] < nums2[j-1])
            return getKth(Arrays.copyOfRange(nums1, i, nums1.length), nums2, k-i);
        else
            return getKth(nums1, Arrays.copyOfRange(nums2, j, nums2.length),  k-j);
    }

    public static double findMedianSortedArrays_v2(int[] nums1, int[] nums2)
    {
        int l = (nums1.length + nums2.length + 1)/2;
        int r = (nums1.length + nums2.length + 2)/2;

        return (getKth(nums1, nums2, l) + getKth(nums1, nums2, r))/2.;
    }
    

    public static void main(String[] args) 
    {
        int[] array1 = {};    
        int[] array2 = {5};    

        double median = findMedianSortedArrays(array1, array2);
        System.out.println(median);


    }                                      
                                           
}
