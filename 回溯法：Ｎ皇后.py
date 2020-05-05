def place(self, k):
    for i in range(k):
        if abs(k - i) == abs(self.solution[k] - self.solution[i]) or self.solution[k] == self.solution[i]:
            return False
    return True


class Nqueen:
    def __init__(self, N):
        self.N = N
        self.sum = 0
        self.solution = [-1] * N
        self.solutionlist = []
        self.depth = 0

    def place(self, k):
        for i in range(k):
            if abs(k - i) == abs(self.solution[k] - self.solution[i]) or self.solution[k] == self.solution[i]:
                return False
        return True

    def back_tracking(self, depth):
        if depth > N - 1:
            self.sum += 1
            #            print self.solution
            self.solutionlist += [self.solution[:]]
        else:
            for i in range(N):
                self.solution[depth] = i
                if self.place(depth):
                    self.back_tracking(depth + 1)
                self.solution[depth] = -1

    def output_nQueen(self):
        self.back_tracking(self.depth)
        return self.solutionlist, self.sum


if __name__ == '__main__':
    N = 4
    nqueen = Nqueen(N)
    list, sum = nqueen.output_nQueen()
