# 포켓 큐브
import numpy as np
from .core import *


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
                    2 : { 'num' : 4, 'index' : 'r0', 'flip' : False },
                    3 : { 'num' : 2, 'index' : 'c1', 'flip' : True },
                    4 : { 'num' : 5, 'index' : 'c0', 'flip' : True },
                    5 : { 'num' : 3, 'index' : 'r1', 'flip' : False },
                }
            },
            'F`' : {
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
            'R' : {
                'rotate' : {
                    'num' : 4,
                    'direction' : 'r',
                },
                'old' : {
                    1 : 'c1',
                    2 : 'r1',
                    5 : 'r0',
                    6 : 'c0'
                },
                'change' : {
                    1 : { 'num' : 4, 'index' : 'r0', 'flip' : False },
                    2 : { 'num' : 2, 'index' : 'c1', 'flip' : True },
                    5 : { 'num' : 5, 'index' : 'c0', 'flip' : True },
                    6 : { 'num' : 3, 'index' : 'r1', 'flip' : False },
                }
            },
            'R`' : {
                'rotate' : {
                    'num' : 4,
                    'direction' : 'r',
                },
                'old' : {
                    1 : 'c1',
                    2 : 'r1',
                    5 : 'r0',
                    6 : 'c0'
                },
                'change' : {
                    1 : { 'num' : 4, 'index' : 'r0', 'flip' : False },
                    2 : { 'num' : 2, 'index' : 'c1', 'flip' : True },
                    5 : { 'num' : 5, 'index' : 'c0', 'flip' : True },
                    6 : { 'num' : 3, 'index' : 'r1', 'flip' : False },
                }
            },
            'U' : {
                'rotate' : {
                    'num' : 2,
                    'direction' : 'r',
                },
                'old' : {
                    1 : 'c1',
                    3 : 'r1',
                    4 : 'r0',
                    6 : 'c0'
                },
                'change' : {
                    1 : { 'num' : 4, 'index' : 'r0', 'flip' : False },
                    3 : { 'num' : 2, 'index' : 'c1', 'flip' : True },
                    4 : { 'num' : 5, 'index' : 'c0', 'flip' : True },
                    6 : { 'num' : 3, 'index' : 'r1', 'flip' : False },
                }
            },
            'U`' : {
                'rotate' : {
                    'num' : 2,
                    'direction' : 'r',
                },
                'old' : {
                    1 : 'c1',
                    3 : 'r1',
                    4 : 'r0',
                    6 : 'c0'
                },
                'change' : {
                    1 : { 'num' : 4, 'index' : 'r0', 'flip' : False },
                    3 : { 'num' : 2, 'index' : 'c1', 'flip' : True },
                    4 : { 'num' : 5, 'index' : 'c0', 'flip' : True },
                    6 : { 'num' : 3, 'index' : 'r1', 'flip' : False },
                }
            },
            'B' : {
                'rotate' : {
                    'num' : 6,
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
            'B`' : {
                'rotate' : {
                    'num' : 6,
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
            'L' : {
                'rotate' : {
                    'num' : 3,
                    'direction' : 'r',
                },
                'old' : {
                    1 : 'c1',
                    2 : 'r1',
                    5 : 'r0',
                    6 : 'c0'
                },
                'change' : {
                    1 : { 'num' : 4, 'index' : 'r0', 'flip' : False },
                    2 : { 'num' : 2, 'index' : 'c1', 'flip' : True },
                    5 : { 'num' : 5, 'index' : 'c0', 'flip' : True },
                    6 : { 'num' : 3, 'index' : 'r1', 'flip' : False },
                }
            },
            'L`' : {
                'rotate' : {
                    'num' : 3,
                    'direction' : 'r',
                },
                'old' : {
                    1 : 'c1',
                    2 : 'r1',
                    5 : 'r0',
                    6 : 'c0'
                },
                'change' : {
                    1 : { 'num' : 4, 'index' : 'r0', 'flip' : False },
                    2 : { 'num' : 2, 'index' : 'c1', 'flip' : True },
                    5 : { 'num' : 5, 'index' : 'c0', 'flip' : True },
                    6 : { 'num' : 3, 'index' : 'r1', 'flip' : False },
                }
            },
            'D' : {
                'rotate' : {
                    'num' : 5,
                    'direction' : 'r',
                },
                'old' : {
                    1 : 'c1',
                    3 : 'r1',
                    4 : 'r0',
                    6 : 'c0'
                },
                'change' : {
                    1 : { 'num' : 4, 'index' : 'r0', 'flip' : False },
                    3 : { 'num' : 2, 'index' : 'c1', 'flip' : True },
                    4 : { 'num' : 5, 'index' : 'c0', 'flip' : True },
                    6 : { 'num' : 3, 'index' : 'r1', 'flip' : False },
                }
            },
            'D`' : {
                'rotate' : {
                    'num' : 5,
                    'direction' : 'r',
                },
                'old' : {
                    1 : 'c1',
                    3 : 'r1',
                    4 : 'r0',
                    6 : 'c0'
                },
                'change' : {
                    1 : { 'num' : 4, 'index' : 'r0', 'flip' : False },
                    3 : { 'num' : 2, 'index' : 'c1', 'flip' : True },
                    4 : { 'num' : 5, 'index' : 'c0', 'flip' : True },
                    6 : { 'num' : 3, 'index' : 'r1', 'flip' : False },
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
