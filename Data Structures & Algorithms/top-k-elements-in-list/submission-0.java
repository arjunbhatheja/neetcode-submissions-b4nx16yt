class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> hm = new HashMap<>();

        for(int num: nums){
            if(hm.containsKey(num)){
                hm.put(num, hm.get(num) + 1);
            }
            else{
                hm.put(num, 1);
            }
        }

        List<List<Integer>> freq = new ArrayList<>(nums.length + 1);
        for (int i = 0; i <= nums.length; i++) freq.add(new ArrayList<>());

        for(Map.Entry<Integer, Integer> entry : hm.entrySet()){
            freq.get(entry.getValue()).add(entry.getKey());
        }

        int index = freq.size() - 1;
        int[] res = new int[k];
        int i = 0;
        while(k!=0){
            for(int n : freq.get(index)){
                res[i] = n;
                i++;
                k--;
                if(k==0){
                    return res;
                }
            }
            index--;
        }
        return res;
    }
}
