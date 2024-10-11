import pygame as pg
import random

class Solveable:
    def __init__(self, board):
        self.board = board
        self.size = len(board)
    
    def inversions(self):  # 반전 수 계산용
        count = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] != 0:
                    # 현재 숫자와 그 뒤에 있는 숫자들을 비교
                    for k in range(i, self.size):
                        for l in range(self.size):
                            # 이전 꺼 무시 and 0무시 and 현 숫자 > 비교숫자
                            if k == i and l <= j and self.board[k][l] != 0 and self.board[i][j] > self.board[k][l]:
                                count += 1  
        return count
    
    def solCheck(self):  # 확인
        count = self.inversions()
        blank = sum(Npuzzle.find_blank()) % 2  # Npuzzle 인스턴스 필요
        if self.size % 2 == 1:  # 홀수일 때
            return count % 2 == 0  # I가 짝수면 True
        else:  # 짝수일 때
            return (blank == 0 and count % 2 == 1) or (blank == 1 and count % 2 == 0)

class makeBoard:
    def __init__(self, size):
        self.size = size
        self.board = self.shuffle([[j * size + i + 1 for i in range(size)] for j in range(size)])
        self.goal = [[j * size + i + 1 for i in range(size)] for j in range(size)]
        self.goal[size - 1][size - 1] = 0
    
    def shuffle(self, board):
        self.board = board
        for _ in range(50):
            shake = random.choice(['up', 'down', 'left', 'right'])
            # player_move를 makeBoard의 메서드로 변경
            self.player_move(shake)
            print(self.board)
        return self.board
    
    def find_blank(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return i, j

    def player_move(self, input):
        x, y = self.find_blank()
        if input == 'up' and x > 0:
            self.board[x][y], self.board[x - 1][y] = self.board[x - 1][y], self.board[x][y]
        elif input == 'down' and x < self.size - 1:
            self.board[x][y], self.board[x + 1][y] = self.board[x + 1][y], self.board[x][y]
        elif input == 'left' and y > 0:
            self.board[x][y], self.board[x][y - 1] = self.board[x][y - 1], self.board[x][y]
        elif input == 'right' and y < self.size - 1:
            self.board[x][y], self.board[x][y + 1] = self.board[x][y + 1], self.board[x][y]

class Npuzzle:
    def __init__(self, size):
        self.board_instance = makeBoard(size)  # makeBoard 인스턴스 생성
        self.board = self.board_instance.board
        self.goal = self.board_instance.goal
        self.size = size
        
    def find_blank(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return i, j
                
    def player_move(self, input):
        x, y = self.find_blank()
        if input == 'up' and x > 0:
            self.board[x][y], self.board[x - 1][y] = self.board[x - 1][y], self.board[x][y]
        elif input == 'down' and x < self.size - 1:
            self.board[x][y], self.board[x + 1][y] = self.board[x + 1][y], self.board[x][y]
        elif input == 'left' and y > 0:
            self.board[x][y], self.board[x][y - 1] = self.board[x][y - 1], self.board[x][y]
        elif input == 'right' and y < self.size - 1:
            self.board[x][y], self.board[x][y + 1] = self.board[x][y + 1], self.board[x][y]
    
    def if_goal(self):
        return self.board == self.goal

# 게임 인스턴스 생성 예시
npuzzle = Npuzzle(3)
