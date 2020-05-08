class Solution{
    public List<string> topKFrequent(String[] words, int k){
        // hash map
        Map<String, Integer> count = new HashMap();
        for (String word: words){
            count.put(word, count.getOrDefault(word, 0) + 1);
        }
        // queue ---> here get the queue  in the order by comparing the number of letter for each key!
        PriorityQueue<String> heap = new PriorityQueue<String>(
            (w1, w2) --> count.get(w1).equals(count.get(w2)) ?
            w2.compareTo(w1) : count.get(w1) - count.get(w2)
        );

        for (String word: count.keySet()){
            heap.offer(word);
            if (heap.size() > k) heap.poll()
        }

        List<String> ans = new ArrayList();
        while (!heap.isEmpty()) ans.add(heap.poll());
        Collections.reverse(ans);
        return ans;
    }
}