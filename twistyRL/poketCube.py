# 포켓 큐브
from .core import *


class poketCube( Cube ) :
    """
    포켓큐브(2*2*2) 게임
    """

    def __init__( self ) :
        self.size = 2
        self.make( self.size )
        self.history = [ ]
        self.done = None
        self.point = None
        self.count = 0
        self.set = ('F', 'F`', 'R', 'R`', 'U', 'U`', 'B', 'B`', 'L', 'L`', 'D', 'D`')

        # todo:랜덤한 값을 대입

        self.check( )

    def __repr__( self ) :
        """
        아래와 같은 구조르 출력됨
        ex) 루빅스큐브 출력시
        |================================|
        |  포켓 큐브 게임 2*2*2             |
        |       -------  완료 여부 : False |
        |       | 1 2 |  점수 : 00        |
        |       | 1 2 |  회전횟수 : 00     |
        | -------------------------      |
        | | 1 2 | 1 2 | 1 2 | 1 2 |      |
        | | 1 2 | 1 2 | 1 2 | 1 2 |      |
        | -------------------------      |
        |       | 1 2 |                  |
        |       | 1 2 |                  |
        |       -------                  |
        |================================|
        기록 :


        :return:
        """
        f1, f2, f3, f4, f5, f6 = self.cube[ 1 ].matrix, self.cube[ 2 ].matrix, self.cube[ 3 ].matrix, self.cube[
            4 ].matrix, self.cube[ 5 ].matrix, self.cube[ 6 ].matrix

        # 큐브 사이즈에 맞게 자동 조절
        # 단일 객체 길이 측정
        sample = len( '{}'.format( f1[ 0 ][ 0 ] ) )
        nullArea = ' ' * (5 + sample * 2)
        stick1Area = '-' * (5 + sample * 2)
        stick2Area = ' ' + '-' * (17 + sample * 8) + '\n'
        str = '=======================================\n'
        str += '  포켓 큐브 게임 2*2*2\n\n'
        str += '{}{}    완료 여부 : {done}\n'.format( nullArea, stick1Area, done=self.done )
        str += '{}| {} {} |    점수      : {point}\n'.format( nullArea, f2[ 0 ][ 0 ], f2[ 0 ][ 1 ], point=self.point )
        str += '{}| {} {} |    회전횟수  : {count}\n'.format( nullArea, f2[ 1 ][ 0 ], f2[ 1 ][ 1 ], count=self.count )
        str += stick2Area
        str += ' | {} {} | {} {} | {} {} | {} {} |\n'.format( f3[ 0 ][ 0 ], f3[ 0 ][ 1 ], f1[ 0 ][ 0 ], f1[ 0 ][ 1 ],
                                                              f4[ 0 ][ 0 ], f4[ 0 ][ 1 ], f6[ 0 ][ 0 ], f6[ 0 ][ 1 ] )
        str += ' | {} {} | {} {} | {} {} | {} {} |\n'.format( f3[ 1 ][ 0 ], f3[ 1 ][ 1 ], f1[ 1 ][ 0 ], f1[ 1 ][ 1 ],
                                                              f4[ 1 ][ 0 ], f4[ 1 ][ 1 ], f6[ 1 ][ 0 ], f6[ 1 ][ 1 ] )
        str += stick2Area
        str += '{}| {} {} |\n'.format( nullArea, f5[ 0 ][ 0 ], f5[ 0 ][ 1 ] )
        str += '{}| {} {} |\n'.format( nullArea, f5[ 1 ][ 0 ], f5[ 1 ][ 1 ] )
        str += '{}{}\n'.format( nullArea, stick1Area )
        str += ' 기록 : {}\n'.format( self.history )
        str += '====================================='
        return str

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

    # todo: 게임 상태를 알려주는 메소드 추가하기, 해당 메소드 실행시 튜블에 완성여부,점수,개별면 상태를 담아 반환한다
    # todo: action 메소드 실행시 큐브상태를 반환하도록 변경

    @checkDouble
    def rotate( self, action ) :
        """
        큐브를 회전시키는 메소드
        :param act: 명령어셋
        :return:
        """
        act = action
        """
        포켓큐브 명령어 셋
        가능한 명령 : F,F`,R,R`,U,U`,B,B`,L,L`,D,D`,F2,R2,U2,B2,L2,D2
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
            'F' : {  # 완료
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
                    2 : { 'num' : 4, 'index' : 'r0', 'flip' : False },
                    3 : { 'num' : 2, 'index' : 'c1', 'flip' : True },
                    4 : { 'num' : 5, 'index' : 'c0', 'flip' : True },
                    5 : { 'num' : 3, 'index' : 'r1', 'flip' : False },
                }
            },
            'F`' : {  # 완료
                'rotate' : {
                    'num' : 1,
                    'direction' : 'l',
                },
                'old' : {
                    2 : 'c1',
                    3 : 'r1',
                    4 : 'r0',
                    5 : 'c0'
                },
                'change' : {
                    2 : { 'num' : 3, 'index' : 'r1', 'flip' : True },
                    3 : { 'num' : 5, 'index' : 'c0', 'flip' : False },
                    4 : { 'num' : 2, 'index' : 'c1', 'flip' : False },
                    5 : { 'num' : 4, 'index' : 'r0', 'flip' : True },
                }
            },
            'R' : {  # 완료
                'rotate' : {
                    'num' : 4,
                    'direction' : 'r',
                },
                'old' : {
                    1 : 'r1',
                    2 : 'r1',
                    5 : 'r1',
                    6 : 'r0'
                },
                'change' : {
                    1 : { 'num' : 2, 'index' : 'r1', 'flip' : False },
                    2 : { 'num' : 6, 'index' : 'r0', 'flip' : True },
                    5 : { 'num' : 1, 'index' : 'r1', 'flip' : False },
                    6 : { 'num' : 5, 'index' : 'r1', 'flip' : True },
                }
            },
            'R`' : {  # 완료
                'rotate' : {
                    'num' : 4,
                    'direction' : 'l',
                },
                'old' : {
                    1 : 'r1',
                    2 : 'r1',
                    5 : 'r1',
                    6 : 'r0'
                },
                'change' : {
                    1 : { 'num' : 5, 'index' : 'r1', 'flip' : False },
                    2 : { 'num' : 1, 'index' : 'r1', 'flip' : False },
                    5 : { 'num' : 6, 'index' : 'r0', 'flip' : True },
                    6 : { 'num' : 2, 'index' : 'r1', 'flip' : True },
                }
            },
            'U' : {  # 완료
                'rotate' : {
                    'num' : 2,
                    'direction' : 'r',
                },
                'old' : {
                    1 : 'c0',
                    3 : 'c0',
                    4 : 'c0',
                    6 : 'c0'
                },
                'change' : {
                    1 : { 'num' : 3, 'index' : 'c0', 'flip' : False },
                    3 : { 'num' : 6, 'index' : 'c0', 'flip' : False },
                    4 : { 'num' : 1, 'index' : 'c0', 'flip' : False },
                    6 : { 'num' : 4, 'index' : 'c0', 'flip' : False },
                }
            },
            'U`' : {  # 완료
                'rotate' : {
                    'num' : 2,
                    'direction' : 'l',
                },
                'old' : {
                    1 : 'c0',
                    3 : 'c0',
                    4 : 'c0',
                    6 : 'c0'
                },
                'change' : {
                    1 : { 'num' : 4, 'index' : 'c0', 'flip' : False },
                    3 : { 'num' : 1, 'index' : 'c0', 'flip' : False },
                    4 : { 'num' : 6, 'index' : 'c0', 'flip' : False },
                    6 : { 'num' : 3, 'index' : 'c0', 'flip' : False },
                }
            },
            'B' : {  # 완료
                'rotate' : {
                    'num' : 6,
                    'direction' : 'r',
                },
                'old' : {
                    2 : 'c0',
                    3 : 'r0',
                    4 : 'r1',
                    5 : 'c1'
                },
                'change' : {
                    2 : { 'num' : 3, 'index' : 'r0', 'flip' : True },
                    3 : { 'num' : 5, 'index' : 'c1', 'flip' : False },
                    4 : { 'num' : 2, 'index' : 'c0', 'flip' : False },
                    5 : { 'num' : 4, 'index' : 'r1', 'flip' : True },
                }
            },
            'B`' : {  # 완료
                'rotate' : {
                    'num' : 6,
                    'direction' : 'l',
                },
                'old' : {
                    2 : 'c0',
                    3 : 'r0',
                    4 : 'r1',
                    5 : 'c1'
                },
                'change' : {
                    2 : { 'num' : 4, 'index' : 'r1', 'flip' : False },
                    3 : { 'num' : 2, 'index' : 'c0', 'flip' : True },
                    4 : { 'num' : 5, 'index' : 'c1', 'flip' : True },
                    5 : { 'num' : 3, 'index' : 'r0', 'flip' : False },
                }
            },
            'L' : {  # 완료
                'rotate' : {
                    'num' : 3,
                    'direction' : 'r',
                },
                'old' : {
                    1 : 'r0',
                    2 : 'r0',
                    5 : 'r0',
                    6 : 'r1'
                },
                'change' : {
                    1 : { 'num' : 5, 'index' : 'r0', 'flip' : False },
                    2 : { 'num' : 1, 'index' : 'r0', 'flip' : False },
                    5 : { 'num' : 6, 'index' : 'r1', 'flip' : True },
                    6 : { 'num' : 2, 'index' : 'r0', 'flip' : True },
                }
            },
            'L`' : {  # 완료
                'rotate' : {
                    'num' : 3,
                    'direction' : 'l',
                },
                'old' : {
                    1 : 'r0',
                    2 : 'r0',
                    5 : 'r0',
                    6 : 'r1'
                },
                'change' : {
                    1 : { 'num' : 2, 'index' : 'r0', 'flip' : False },
                    2 : { 'num' : 6, 'index' : 'r1', 'flip' : True },
                    5 : { 'num' : 1, 'index' : 'r0', 'flip' : False },
                    6 : { 'num' : 5, 'index' : 'r0', 'flip' : True },
                }
            },
            'D' : {  # 완료
                'rotate' : {
                    'num' : 5,
                    'direction' : 'r',
                },
                'old' : {
                    1 : 'c1',
                    3 : 'c1',
                    4 : 'c1',
                    6 : 'c1'
                },
                'change' : {
                    1 : { 'num' : 4, 'index' : 'c1', 'flip' : False },
                    3 : { 'num' : 1, 'index' : 'c1', 'flip' : False },
                    4 : { 'num' : 6, 'index' : 'c1', 'flip' : False },
                    6 : { 'num' : 3, 'index' : 'c1', 'flip' : False },
                }
            },
            'D`' : {  # 완료
                'rotate' : {
                    'num' : 5,
                    'direction' : 'l',
                },
                'old' : {
                    1 : 'c1',
                    3 : 'c1',
                    4 : 'c1',
                    6 : 'c1'
                },
                'change' : {
                    1 : { 'num' : 3, 'index' : 'c1', 'flip' : False },
                    3 : { 'num' : 6, 'index' : 'c1', 'flip' : False },
                    4 : { 'num' : 1, 'index' : 'c1', 'flip' : False },
                    6 : { 'num' : 4, 'index' : 'c1', 'flip' : False },
                }
            },
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
