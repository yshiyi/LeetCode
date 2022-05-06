"""
input: “test”

output: [“test”, “1est”, “t1st”, “te1t”, “tes1”, 
         “2st”, “t2t”, “te2", 
         “1e1t”, “1es1", “t1s1”, 
         “1e2", “2s1”, 
         “3t”, “t3”, 
         “4"]

public List<String> conversionCombination(String s) {
        List<String> ans = new ArrayList<>();
        for (int len = 0; len < s.length(); len++) {
            for (int i = 0; i + len < s.length(); i++) {
                ans.add(s.substring(0,i)+String.valueOf(len+1)+s.substring(i+len+1));
            }
        }
        return ans;
    }

"""
