public class FunWithPalindrome{
    /*
 * Complete the function below.
 */

    static int funPal(String s) {
        //length of s
        int n = s.length();

        if(n<=1){
            return n;
        }

        //to store the length of palindromes
        int dp[][] = new int[n][n];

        //Single characters are always palindrome
        for(int i=0;i<n;i++){
            dp[i][i] = 1;
        }

        for(int l = 2; l <= n; l++){
            for(int i = 0; i < n-l + 1; i++){
                int j = i + l - 1;
                if(l == 2 && s.charAt(i) == s.charAt(j)){
                    dp[i][j] = 2;
                }else if(s.charAt(i) == s.charAt(j)){
                    dp[i][j] = dp[i + 1][j-1] + 2;
                }else{
                    dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }


        int prod = 0;
        for(int i=1;i<n;i++){
            int temp = dp[0][i-1]* dp[i][n-1];
            if(temp>prod){
                prod = temp;
            }
        }
        return prod;

    }

}