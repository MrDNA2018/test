# 给定 n 个作业的集合 j = {j1, j2, …, jn}。每一个作业 j[i] 都有两项任务分别在两台机器上完成。每一个作业必须先由机器1 处理，然后由机器2处理。作业 j[i] 需要机器 j 的处理时间为 t[j][i] ，其中i = 1, 2, …, n, j = 1, 2。对于一个确定的作业调度，设F[j][i]是作业 i 在机器 j 上的完成处理的时间。所有作业在机器2上完成处理的时间之和 f = sigma F[2][i] 称为该作业调度的完成时间之和。
# 批处理作业调度问题要求对于给定的 n 个作业，制定最佳作业调度方案，使其完成时间和达到最小。
class FlowShop:
    def __init__(self, N, mission):
        self.N = N  # 作业数目
        self.mission = mission  # 作业时间
        self.bestFinishtime = 10000  # 最优完成时间
        self.schedule = [i for i in range(N)]  # 当前的策略
        self.bestSchedule = [0] * N  # 最优策略
        self.f2 = [0] * N  # 机器２每个任务完成处理的时间
        self.f1 = 0  # 机器１任务完成处理的时间
        self.totaltime = 0  # 机器２每个任务完成处理的时间，求和，这个时间是每个作业完成时间之和
        self.depth = 0  #

    def back_tracking(self, depth):
        # 递归出口
        if depth > self.N - 1:
            self.bestFinishtime = self.totaltime
            self.bestSchedule[:] = self.schedule[:]
            return
            # 机器１作业时间
        else:
            for i in range(depth, self.N):
                self.f1 += self.mission[0][self.schedule[i]]
                # 机器２作业完成时间
                if depth == 0:
                    self.f2[depth] = self.f1 + self.mission[1][self.schedule[i]]
                else:
                    self.f2[depth] = max(self.f1, self.f2[depth - 1]) + self.mission[1][self.schedule[i]]
                #   这个时间是每个作业完成时间之和，为了让每个作业尽可能早的完成
                self.totaltime += self.f2[depth]
                # 　满足条件，进入下一层处理，这个看成一个模块
                if self.totaltime < self.bestFinishtime:
                    self.schedule[i], self.schedule[depth] = self.schedule[depth], self.schedule[i]
                    self.back_tracking(depth + 1)
                    self.schedule[i], self.schedule[depth] = self.schedule[depth], self.schedule[i]
                # 　  回溯处理，又可以理解为没有进入下一层，对上面操作进行undo回溯
                self.f1 -= self.mission[0][self.schedule[i]]
                self.totaltime -= self.f2[depth]

    def print_back_tracking(self):
        self.back_tracking(self.depth)
        print
        self.bestSchedule
        print
        self.bestFinishtime


N = 3
mission = [[2, 3, 2], [1, 1, 3]]
instance = FlowShop(N, mission)
instance.print_back_tracking()


