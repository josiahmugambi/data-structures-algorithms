# python3

class ParallelProcessing:
        
    def read_data(self):
        #self.n_workers, m_jobs = (4,20)
        #self.job_durations = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.n_workers, m_jobs = map(int, input().split())
        self.job_durations = list(map(int, input().split()))
        assert m_jobs == len(self.job_durations)
    
    def left_child(self, i):
  #      return 2*i + 1
        return 2*i
    
    def right_child(self, i):
#        return 2*i + 2
        return 2*i + 1
    
    def parent(self, i):
        return (i - 1) //2
        
    def sift_down(self, i):
        size = len(self.nodes) - 1
        min_index = i 
        l = self.left_child(i) 
        r = self.right_child(i)  
        
        if l <= size:
            if self.nodes[l][1] < self.nodes[min_index][1]:
                min_index = l
            elif self.nodes[l][1] == self.nodes[min_index][1] and self.nodes[l][0] < self.nodes[min_index][0]:
                min_index = l
                
        if r <= size:
            if self.nodes[r][1] < self.nodes[min_index][1]:
                min_index = r
            elif self.nodes[r][1] == self.nodes[min_index][1] and self.nodes[r][0] < self.nodes[min_index][0]:
                min_index = r 
        
        if i != min_index:
            self.nodes[i], self.nodes[min_index] = self.nodes[min_index], self.nodes[i]
            self.sift_down(min_index)
        
    def assign_jobs(self):
        self.assigned_worker = [None] * len(self.job_durations)
        self.start_time = [None] * len(self.job_durations)
        #self.assigned_job = namedtuple("AssignedJob", ["worker", "started_at"])
        self.nodes = [None] + [[x,0] for x in range(self.n_workers)]
        for d in range (len(self.job_durations)):
            self.assigned_worker[d] = self.nodes[1][0]
            self.start_time[d] = self.nodes[1][1]
            self.nodes[1][1] += self.job_durations[d]
            self.sift_down(1)
        
    def print_result(self):
        for j in range(len(self.job_durations)):
            print(self.assigned_worker[j], self.start_time[j])

if __name__ == "__main__":
    pp = ParallelProcessing()
    pp.read_data()
    pp.assign_jobs()
    pp.print_result()
