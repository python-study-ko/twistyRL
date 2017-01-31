import numpy as np
from functools import wraps
import random

"""
큐브 게임을 위한 핵식 클래스 모음
"""


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
        self.check( )

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

    def getface( self ) :
        """
        n*n 행열을 1차 행열로 넘겨줍니다.
        :return:
        """
        return np.reshape( self.matrix, (1, pow( self.size, 2 )) )

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


# 두번 반복 명령어 인식 데코레이터
def checkDouble( func ) :
    @wraps( func )
    def wrapper( *args ) :
        if args[ 1 ][ -1 ] == '2' :
            # 명령어 끝에 2가 있을 경우 해당 명령어 2번 반복
            act = args[ 1 ][ :-1 ]
            for _ in range( 2 ) :
                func( args[ 0 ], act )
        else :
            func( *args )

    return wrapper


class Cube :
    """
    큐브 생성 관리에 유용한 메소드 모음
    """


    def __init__( self ) :
        """
        정적 변수는 여기에서 초기화 하구 이후 activeInit을 실행 하여 동적 변수를 생성한다.
        """
        self.history = [ ]
        self.size = 0  # 큐브 크기
        self.point = 0
        self.set = None  # 사용가능한 회전 명령어 모음
        self.scram = [ ]  # 사용된 스크램블

        # 이 클래스를 상속 받을 경우 아래와 같이 동적 변수를 초기화 시켜줘야 합니다
        # self.activaInit()


    def activeInit( self ) :
        """
        고정 메소드에 따라 동적으로 실행될 메소드 목록
        큐브 게임을 만들때 고정 변수를 초기화 한뒤 항상 이 함수를 실행하여 각 큐브에 맞게 실행한다.
        :return:
        """
        # 큐브 생성
        self.make()


    def reset( self ) :
        """
        큐브 초기화
        :return:
        """
        self.history = [ ]
        self.point = 0
        self.scram = [ ]
        for i in range( 1, 7 ) :
            self.cube[ i ].reset( i )

    def make( self ) :
        """
        큐브는 딕셔너리(ey = 면의 인덱스 번호, value = 면 인스턴스)로 구성되있다.
        면에 인덱스 번호를 부여하는 방식은 READMD.md파일의 큐브 배치도를 참고 바람.
        모든 행동은 1번 면이 가장 앞에 있는 상태를 기준으로 이뤄진다.
        :return:
        """
        # self.size를 지정 하지 않았을 경우 에러 발생
        assert self.size != 0
        # 큐브 초기화
        self.cube = { }
        # 큐브 생성
        for i in range( 1, 7 ) :
            # 면을 생성한다.
            self.cube[ i ] = face( self.size )
            # 면의 값을 초기화 시킨다 ex) 3번 면의 값은 모두 3으로 초기화
            self.cube[ i ].reset( i )


    ## 여러 상태를 체크하는 동적 변수
    @property
    def faces(self):
        # 머신러닝에 사용할 면 상태
        faces = None
        for i in range( 1, 7 ) :
            face = self.cube[ i ]
            if i == 1 :
                faces = face.getface( )
            else :
                faces = np.append( faces, face.getface( ), axis=0 )
        return faces

    @property
    def count( self ) :
        # 큐브 회전 횟수
        return len( self.history )

    @property
    def facePoint( self ) :
        # 완성된 면에 부여할 점수
        return pow( self.size, 2 )

    @property
    def facesDone( self ) :
        # 면들의 완성 여부
        return [ self.cube[ x ].done for x in self.cube ]

    @property
    def doneCount( self ) :
        return self.facesDone.count( True )

    @property
    def lastAct( self ) :
        # 마지막으로 실행한 명령어
        return self.history[ -1 ] if len( self.history ) != 0 else None

    @property
    def done(self):
        # 큐브 완성 여부 확인: 모든 면이 완성 됬을 경우 큐브가 완성 되었다고 표시한다.
        return False if False in self.facesDone else True

    @property
    def reward(self):
        """
        각 상황에 따른 보상 점수를 계산한다.
        :return: 보상 점수
        """
        if self.count == 0:
            # 게임 시작 전일 경우 보상은 0
            return 0
        elif True in self.facesDone:
            # 완성된 면이 존재할 경우 완성된 면의 갯수*면의 총점수/회전횟수 만큼 보상을 줘서
            # 많이 회전할수록 점수가 떨어지게 함 즉 단순 회전을 반복하여 고득점하는 기회를 없앰
            return self.facePoint*self.doneCount/self.count
        else:
            # 미완성일 경우 점수를 주지 않는다
            return 0


    def __repr__( self ) :
        """
        아래와 같은 구조르 출력됨
        ex) 루빅스큐브 출력시
        |=====================================|
        |  3*3*3 큐브 게임                      |
        |         ---------                   |
        |         | 1 2 3 |  완료 여부 : False  |
        |         | 1 2 3 |  점수 : 00         |
        |         | 1 2 3 |  회전횟수 : 00      |
        | ---------------------------------   |
        | | 1 2 3 | 1 2 3 | 1 2 3 | 1 2 3 |   |
        | | 1 2 3 | 1 2 3 | 1 2 3 | 1 2 3 |   |
        | | 1 2 3 | 1 2 3 | 1 2 3 | 1 2 3 |   |
        | ---------------------------------   |
        |         ---------                   |
        |         | 1 2 3 |                   |
        |         | 1 2 3 |                   |
        |         | 1 2 3 |                   |
        |         ---------                   |
        |=====================================|
        기록 :


        :return:
        """

    @checkDouble  # 반복명령어 처리 데코레이터
    def rotate( self, action ) :
        """
        입력받은 회전방향으로 큐브를 돌린다.
        각 큐브 게임에서 오버라이팅해서 사용하면 됨
        또한 반복명령어(ex. F2, F`2)를 처리하고 싶으면 @checkDouble 데코레이터를 달아주면 된다
        :param action:
        :return:
        """
        pass

    def action( self, action ) :
        """
        입력받은 act를 수행한뒤 상태를 반환해준다
        :param act: 회전 방향 기호
        :return: (완료여부,점수,회전횟수,큐브화면)
        """
        self.rotate( action )
        # 회전 기록
        self.history.append( action )
        # todo:180되 회전 명령어대신 90도 명령어가 2번 표기 되도록 변경
        self.point += self.reward

        return (self.done, self.reward, self.count, self.faces)

    def scramble( self, len=25, count=2, checkface=1, hide=True ) :
        """
        램덤한 5개의 스크램블을 생성한뒤 램덤으로 하나의 스크램블을 선택하여 큐브 모양을 만들어 준다.
        :param len: 스크램블 길이
        :param count: 생성할 스크램블 갯수
        :param checkface: 스크램블이 제대로 됬는지 확인하는 기준 완성된 면이 해당값 이하일때만 통과시킨다. 저수준의 학습시 유용함
        :param hide: 스크램블을 출력할지 여부, 출력여부와 상관없이 self.scramble에 저장은 된다.
        :return:
        """
        # 큐브 초기화
        self.reset( )

        # 임의의 스크램블 모음
        scrambles = [ ]
        # 사용가능한 명령어 모음
        set = self.set

        lenth = len
        num = count

        def mix( ) :
            """
            스크램블을 만든다
            :return:
            """
            scramble = [ ]
            for _ in range( lenth ) :
                # 스크램블에 임의의 명령어 추가
                scramble.append( random.choice( set ) )
            # 완성된 스크램블 순서를 뒤섞기
            random.shuffle( scramble )
            return scramble

        # 완성된 면이 한면 두면 이상이 안될때까지 스크램블 반복

        while True :
            for _ in range( num ) :
                scrambles.append( mix( ) )

            # 스크램블 선택
            self.scram = random.choice( scrambles )

            # 스크램블 하기
            for r in self.scram :
                self.rotate( r )

            # 스크램블 순서를 보여준다
            if not hide :
                print( "scramble by ", self.scram )

            if self.doneCount <= checkface :
                break

        return self.faces
