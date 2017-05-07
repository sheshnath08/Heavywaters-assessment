public class GridLand{

    static String[] gridLand(String[] inp) {

        //Using the constraint specified in the problem
        //DP stores the length of  path to i,j from 0,0
        int dp[][] = new int[11][11];

        for(int i = 0; i<11; i++){
            dp[i][0] = 1;
        }
        for(int j = 0; j<11; j++)
        {
            dp[0][j] = 1;
        }
        for(int i = 1; i<11; i++) {
            for(int j =1; j<11; j++) {
                dp[i][j] = dp[i-1][j]+dp[i][j-1];
            }
        }

        ArrayList<String> res = new ArrayList<String>();

        for(int i=0; i<inp.length; i++) {
            String s = inp[i];
            int x, y, k;
            String[] ss = s.split(" ");
            x=Integer.parseInt(ss[0]);
            y=Integer.parseInt(ss[1]);
            k=Integer.parseInt(ss[2]);
            k+=1;
            String result = "";

            while(x>0&&y>0) {

                if(dp[x-1][y]>=k) {
                    result+="H";
                    x--;
                }
                else {
                    result += "V";
                    k-=dp[x-1][y];
                    y--;
                }

            }

            while(y>0){
                result+="V";
                y--;
            }

            while(x>0){
                result+="H";
                x--;
            }

            res.add(result);

        }

        String[] r = new String[res.size()];

        for(int i=0; i<res.size(); i++){
            r[i] = res.get(i);
        }
        return r;
    }

}