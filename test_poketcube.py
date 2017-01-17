from cuvenv import *


def testpoket( ) :
    """
    포켓큐브 회전 개발용 테스트 함수
    :return:
    """

    sampleCube = {
        1 : [ [ 11, 12 ], [ 13, 14 ] ], 2 : [ [ 21, 22 ], [ 23, 24 ] ], 3 : [ [ 31, 32 ], [ 33, 34 ] ],
        4 : [ [ 41, 42 ], [ 43, 44 ] ], 5 : [ [ 51, 52 ], [ 53, 54 ] ], 6 : [ [ 61, 62 ], [ 63, 64 ] ]
    }

    def reset( cube ) :
        for i in range( 1, 7 ) :
            cube.cube[ i ].set( sampleCube[ i ] )
            cube.history = []
        return cube

    # 회전 테스트
    poket = poketCube( )
    # turnset = ('F', 'F`', 'R', 'R`', 'U', 'U`', 'B', 'B`', 'L', 'L`', 'D', 'D`')
    turnset = ('F')

    print( "회전 테스트" )
    for act in turnset:
        poket = reset(poket)
        poket.action(act)
        print("{act} 실행:\n{cube}".format(act=act,cube=poket))


if __name__ == "__main__" :
    ## 테스트 코드
    # 포켓큐브 생성
    poket = poketCube( )
    print( "큐브 생성\n", poket )

    testpoket( )
