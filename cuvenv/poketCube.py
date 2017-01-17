# n*n*n 포켓 큐브
import numpy as np


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

    def __repr__( self ) :

        return "\n" + str( self.matrix ) + "\n"

    def reset( self, num ) :
        """
        면의 모든 숫자를 num으로 바꿔준다
        큐브 초기 생성시 면 값을 리셋 시키기 위한 함수
        :param num:
        :return:
        """
        self.matrix[ :, : ] = num

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
            return np.copy( self.matrix[ :, indexcode ] )
        elif index[ 0 ] == "c" :
            return np.copy( self.matrix[ indexcode, : ] )

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

    def rotate( self, Direction="r" ) :
        """
        면을 오른쪽 혹은 왼쪽으로 회전한다.
        기본은 오른쪽으로 회전
        :param count: (r :오른쪽으로 회전, l: 왼쪽으로 회전)
        :return:
        """
        # 방향 값 확인
        direc = Direction
        assert direc in ('r', 'l')

        if direc == 'r' :
            self.matrix = np.rot90( self.matrix, 3 )
        elif direc == 'l' :
            self.matrix = np.rot90( self.matrix )

        # 상태 갱신
        self.check( )


class Cube :
    """
    큐브 생성 관리에 유용한 메소드 모음
    """

    def make( self, n ) :
        """
        큐브는 딕셔너리(ey = 면의 인덱스 번호, value = 면 인스턴스)로 구성되있다.
        면에 인덱스 번호를 부여하는 방식은 READMD.md파일의 큐브 배치도를 참고 바람.
        모든 행동은 1번 면이 가장 앞에 있는 상태를 기준으로 이뤄진다.
        :param n: 생성할 큐브 차원
        :return:
        """
        size = n

        self.cube = { }
        for i in range( 1, 7 ) :
            # 면을 생성한다.
            self.cube[ i ] = face( size )
            # 면의 값을 초기화 시킨다 ex) 3번 면의 값은 모두 3으로 초기화
            self.cube[ i ].reset( i )

    def check( self ) :
        """
        면 상태 체크 메소드, 큐브가 변경되는 시점마다 호출하여 완셩여부와 점수를 확인한다.
        :return:
        """
        # todo: 메소드 완성하기


class poketCube( Cube ) :
    """
    포켓큐브(2*2*2) 게임
    """

    def __init__( self ) :
        self.make( 2 )

    def copy( self, faces ) :
        """
        딕셔너리에 적혀 있는대로 면을 복사해 준다
        :param faces: 키는 면의 인덱스, 값은 복사할 값이 있는 인덱스
        :return:

        faces = {1:'r1', 2: 'c0}
        dic = self.copy(faces)
        dic == {1:<1번면의 r1 값>, 2: <2번면의 c0 값>}
        """
        dic = faces
        assert type( dic ) == type( dict( ) )

        for i in dic :
            # 면에서 원하는 인덱스 값을 복사하여 알려준다
            dic[ i ] = self.cube[ i ].get( dic[ i ] )
        return dic

    # todo: np.flip(mat,0) 와 np.fliplr(mat)을 이용하여

    def action( self, action ) :
        """
        큐브를 회전시키는 메소드
        :param act: 명령어셋
        :return:
        """
        act = action
        """
        포켓큐브 명령어 셋
        가능한 명령 : F,F`,R,R`,U,U`,B,B`,L,L`,D,D`
        각 명령어에는 명령어 실행시 변경되는 정보를 딕셔너리로 담고 있다.

        rotate : 명령어 실행시 회전하는 면과 회전되는 방향
                num : 회전할 면 번호
                direction : 회전하는 방향

        old : 변경전 상태 캡쳐
                형식 -> key: 면 번호, value: 캡쳐할 부분(바뀌는 부분)
        change : 변경될 부분에 대한 정보
                형식 -> key: 변경될 부분의 면, value: 변경할 부분의 면 (면 번호,변경될 부분, 자료 반전 여부/True: 변경전 자료 반전시키기)

        """
        turnset = {
            'F' : {
                'rotate' : {
                    'num' : 1,
                    'direction' : 'r',
                },
                'old' : {
                    2 : 'c1',
                    3 : 'r1',
                    4 : 'r0',
                    5 : 'c0'
                },
                'change' : {
                    2 : {
                        'num' : 4,
                        'index' : 'r0',
                        'flip' : False,
                    },
                    3 : {
                        'num' : 2,
                        'index' : 'c1',
                        'flip' : True,
                    },
                    4 : {
                        'num' : 5,
                        'index' : 'c0',
                        'flip' : True,
                    },
                    5 : {
                        'num' : 3,
                        'index' : 'r1',
                        'flip' : False,
                    },
                }
            },
            'F`' : 1, 'R' : 4, 'R`' : 4, 'U' : 2, 'U`' : 2, 'B' : 6, 'B`' : 6, 'L' : 3, 'L`' : 3, 'D' : 5,
            'D`' : 5
        }
        # 명령어셋 확인
        assert act in turnset

        ## 명령어셋 호출
        act = turnset[ act ]
        rotate = act[ 'rotate' ]  # 회전할 면
        old = act[ 'old' ]  # 변경될 영역
        change = act[ 'change' ]  # 변경할 영역

        ## 면 회전
        self.cube[ rotate[ 'num' ] ].rotate( rotate[ 'direction' ] )

        ## 면 변경
        # 면 변경을 위해 이전 면 상태 캡쳐
        old = self.copy( old )

        for oldnum in old :
            # 변경될 자료
            data = old[ oldnum ]
            # 변경할 면과 위치
            new = change[ oldnum ]

            # 자료 변경전 자료를 반전 시키기
            if new[ 'flip' ] :
                data = np.flip( data, 0 )

            # 자료 변경
            self.cube[ new[ 'num' ] ].change( new[ 'index' ], data )

