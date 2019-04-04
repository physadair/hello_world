public class MyAtoi
{
    public int myAtoi(String str)
    {
        String digits = "1234567890";
        String signs = "+-";
        


        str = str.trim();
        int num = 0;
        int factor = 1;
        int d;
        for (int i=0; i<str.length(); i++) {
            if (i == 0 && str.charAt(i) == '-')
                factor = -1;
            else if (i == 0 && str.charAt(i) == '+')
                factor = 1;
            else if (digits.indexOf(str.charAt(i)) != -1) {
              	d = (int) (str.charAt(i) - '0')  
				if ((factor*num < Integer.MIN_VALUE/10) ||
                    (factor*num == Integer.MIN_VALUE/10 && d > 8))
                    return Integer.MIN_VALUE;
                else if ((factor*num > Integer.MAX_VALUE/10) ||
                        (factor*num == Integer.MAX_VALUE/10 && d > 7)) {
                    return Integer.MAX_VALUE;}
                num = 10*num + d;
            }
            else
                break;
        }
        return factor*num;
	}
}
