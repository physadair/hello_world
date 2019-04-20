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
    

    public static void main(String[] args) 
    {
        int[] array1 = {};    
        int[] array2 = {5};    

        double median = findMedianSortedArrays(array1, array2);
        System.out.println(median);


    }                                      
                                           
}
