# n*n*n 포켓 큐브
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
        dtype = np.uint8
        self.size = n
        self.matrix = np.zeros( (self.size, self.size), dtype=dtype )

    def set( self, mat ) :
        """
        면의 초기값을 mat로 바꿔준다
        :param mat: ndarray 혹은 차원이 동일한 리스트로 만든 행렬
        :return:
        """
        newmat = mat

        # ndarray 형식 일 경우
        if type( newmat ) == type( self.matrix ) :
            # mat의 자료형 비교
            if not newmat.dtype == self.matrix.dtype :
                # 자료형이 맞지 않을 경우 face객체의 행렬과 자료형을 동일하게 변경
                newmat.dtype = self.matrix.dtype

        # 리스트 형식의 행렬일 경우
        elif type( newmat ) == type( list( ) ) :
            # 리스트를 ndarray 타입으로 변경
            newmat = np.array( newmat, dtype=self.matrix.dtype )

        # mat의 shape 비교
        assert newmat.shape == self.matrix.shape

        self.matrix = newmat
        self.check( )

    def check( self ) :
        """
        면의 상태정보를 갱신해 준다. 자료가 변경될때 이 메소드를 호출해 주면 자동으로 갱신한다.
        self.done은 면의 완성여부를 self.point는 면의 점수를 알려준다.
        점수는 면에 가장 많이 중복된 숫자의 갯수로 매겨진다.
        루빅스 큐브를 예로 들면 한 면에서 최대 9점이 나올수 있으며 루빅스 큐브 한개에서 최대 54점이 나온다.
        :return:
        """

        num, count = np.unique( self.matrix, return_counts=True )

        # 한면에 있는 숫자와 갯수
        # ex) [[1,2,1],[2,3,1],[2,4,1]] 일 경우 -> self.status == [(1, 4), (2, 3), (3, 1), (4, 1)]
        self.status = list( zip( num, count ) )
        if len( self.status ) == 1 :  # 한면의 모든 숫자가 동일할 경우
            self.done = True
        else :
            self.done = False

        self.point = self.status[ 0 ][ 1 ]

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

    def row2col( self, row ) :
        """
        열을 행으로 바꿔준다.
        ex)
            [[1],[2],[3]] -> [1,2,3]
        :param row:
        :return: col
        """
        transrow = row
        transcol = [ ]
        for num in transrow :
            transcol.append( num[ 0 ] )
        return transcol

    def col2row( self, col ) :
        """
        행을 열로 바꿔준다.
        ex)
            [1,2,3] -> [[1],[2],[3]]
        :param col:
        :return: row
        """
        transcol = col
        transrow = [ ]

        for num in transcol :
            transrow.append( [ num ] )
        return transrow

    def get( self, index ) :
        """
        해당 인덱스의 값을 넘겨준다
        :param index: 열,행과 인덱스 번호로 이뤄진 텍스트 ex) "r0", "c4"
        :return:
        """
        indexcode = int( index[ 1 : ] )

        if index[ 0 ] == "r" :
            return self.matrix[ :, indexcode ]
        elif index[ 0 ] == "c" :
            return self.matrix[ indexcode, : ]

    def change( self, index, data ) :
        """
        입력받은 인덱스의 값을 바꿔준다
        :param index:
        :param data:
        :return:
        """

        ## 인덱싱문구 해석

        # 인덱싱 번호
        indexcode = int( index[ 1 : ] )

        if index[ 0 ] == "r" :
            self.matrix[ :, indexcode ] = data
        elif index[ 0 ] == "c" :
            self.matrix[ indexcode, : ] = data

        # 상태갱신
        self.check( )


if __name__ == "__main__" :
    ## 테스트 코드

    # face 객체 테스트
    sample1 = [ [ 1, 6, 4 ], [ 2, 4, 1 ], [ 4, 5, 1 ] ]
    sample1np = np.array( sample1,dtype=np.uint8 )
    sample2 = [ [ 1, 1, 1 ], [ 1, 1, 1 ], [ 1, 1, 1 ] ]
    n = 3
    newface = face( 3 )

    # n*n의 면 생성
    print( "{n}*{n} 면 생성\n면 상태:\n{matrix}".format( n=n, matrix=newface.matrix ) )

    print( "\n면에 리스트 타입의 값을 부여" )
    newface.set( sample1 )
    print( "값 부여\n면 상태:\n{matrix}\n완셩여부: {done} 면 점수: {point}".format( matrix=newface.matrix, done=newface.done,
                                                                         point=newface.point ) )
    print( "\nndarray 타입의 값을 부여" )
    newface.set( sample1np )
    print( "값 부여\n면 상태:\n{matrix}\n완셩여부: {done} 면 점수: {point}".format( matrix=newface.matrix, done=newface.done,
                                                                         point=newface.point ) )
    # 면이 완성 됬을 경우
    newface.set( sample2 )
    print( "\n값 부여\n면 상태:\n{matrix}\n완셩여부: {done} 면 점수: {point}".format( matrix=newface.matrix, done=newface.done,
                                                                         point=newface.point ) )
