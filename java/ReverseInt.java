public class Solution
{
    public static int reverse_v0(int x)
    {
        long r = 0;
        while (true)
        {
            if (x == 0) break;
            r = r*10 + x%10;
            x = x/10;
        }
        if (r < Integer.MIN_VALUE || r > Integer.MAX_VALUE) 
            r = 0;
        
        return  (int) r;
    }
    
	public static int reverse_v1(int x)
    {
        int r = 0;
        while (true)
        {
            if (x == 0) break;
            if (r < Integer.MIN_VALUE/10 || r > Integer.MAX_VALUE/10) 
                return 0;
            r = r*10 + x%10;
            x = x/10;
        }
        
        return  (int) r;
    }

    public static int reverse(int x)
    {
        return reverse_1(x);
    }
}
