# 2*2*2 포켓 큐브
import numpy as np
import operator


class face :
    """
    큐브의 면을 표현 하는 객체
    큐브의 색(숫자)을 바꿔준다.
    """

    def __init__( self, n ) :
        """
        n*n 크기의 면의 만든다
        :param n:
        :return:
        """
        self.size = n
        self.matrix = np.zeros( (self.size, self.size), dtype=np.uint8 )

    def set( self, mat ) :
        self.mat = np.array( mat )

        # 크기를 확인하여 오류를 예방
        assert self.mat.shape == (self.size, self.size)

        self.matrix = np.array( mat, dtype=np.uint8 )

    def check( self ) :
        """
        해당 면이 가지고 있는 접수를 알려준다.
        점수는 면에 있는 숫자 1~6중에서 가장 많이 중복된 갯수임
        루빅스 큐브를 예로 들면 한 면에서 최대 9점이 나올수 있으며 루빅스 큐브 한개에서 최대 54점이 나온다.
        :return:
        """
        # 숫자 갯수 확인용
        self.numcount = dict( )

        # 면 속에 있는 전체 숫자 확인
        for row in self.matrix :
            for col in row :
                if col in self.numcount :
                    # 이미 딕셔너리에 숫자가 존재할경우 카운팅만함
                    self.numcount[ col ] += 1
                else :
                    # 딕셔너리에 존재 하지 않는 숫자면 셋에 추가후 카운팅
                    self.numcount[ col ] = 1

        if len( self.numcount ) == 1 :
            # 한면의 모든 숫자가 일치할경우 최대 점수 부여
            return True, pow( self.size, 2 )
        else :
            # 값을 기준으로 정렬후 제일 높음 점수를 내보내기
            return False, sorted( self.numcount.items( ), key=operator.itemgetter( 1 ), reversed=True )[ 0 ][ 1 ]

    """
    액션 메소드
    열(row)과 행(col), 인덱싱으로 구분하며 선택된 것은 1로 표시됨
        _____       _____
        |0|0|       |0|1|
        --+--  -->  --+--
        |0|0|       |0|1|
        -----       -----

        왼쪽에서 r1은 [:,:1] 이것과 같은 의미와 위에처럼 표시한다.
    """

    def row2col(self,row):
        """
        열을 행으로 바꿔준다.
        ex)
            [[1],[2],[3]] -> [1,2,3]
        :param row:
        :return: col
        """
        transrow = row
        transcol = []
        for num in transrow:
            transcol.append(num[0])
        return transcol


    def col2row(self,col):
        """
        행을 열로 바꿔준다.
        ex)
            [1,2,3] -> [[1],[2],[3]]
        :param col:
        :return: row
        """
        transcol = col
        transrow = []

        for num in transcol:
            transrow.append([num])
        return transrow

    def change( self, index, data ) :
        """
        입력받은 인덱스의 값을 바꿔준다
        :param index:
        :param data:
        :return:
        """
        
