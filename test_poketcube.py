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

    def reset( cube, mat=sampleCube ) :
        for i in range( 1, 7 ) :
            cube.cube[ i ].set( mat[ i ] )
            cube.history = [ ]
        return cube

    # 회전 테스트
    poket = poketCube( )

    turnset = ('F', 'F`', 'R', 'R`', 'U', 'U`', 'B', 'B`', 'L', 'L`', 'D', 'D`')
    # 180도 회전 명령어
    double = [ x + '2' for x in turnset if x[ -1 ] != '`' ]

    print( "회전 테스트" )
    for act in turnset :
        poket = reset( poket )
        poket.action( act )
        print( "{act} 실행:\n{cube}".format( act=act, cube=poket ) )

    print( "180도 회전 테스트" )
    for act in double :
        poket = reset( poket )
        poket.action( act )
        print( "{act} 실행:\n{cube}".format( act=act, cube=poket ) )

    # 실제로 퍼즐이 맞춰지는지 테스트
    print( "============\n실제 테스트\n섞어 놓은 큐브와 해답을 이용하여 제대로 맞춰지는지 검증" )
    Q = {
        1 : [ [ 3, 2 ], [ 6, 3 ] ], 2 : [ [ 1, 1 ], [ 6, 3 ] ], 3 : [ [ 5, 5 ], [ 1, 2 ] ],
        4 : [ [ 6, 5 ], [ 2, 6 ] ], 5 : [ [ 4, 1 ], [ 2, 4 ] ], 6 : [ [ 4, 3 ], [ 5, 4 ] ]
    }
    solve = [ 'F`', 'F`', 'U`', 'U`', 'F`', 'U', 'R', 'U`', 'F`', 'F`', 'U`', 'U`', 'F`', 'F`' ]

    poket = poketCube( )
    poket = reset( poket, Q )

    for act in solve :
        done, point, count, _ = poket.action( act )
        print( "{}. 회전방향: {} | 완료여부: {} | 점수: {}".format( count, act, done, point ) )
    print( poket )


if __name__ == "__main__" :
    ## 테스트 코드
    # 포켓큐브 생성
    poket = poketCube( )
    print( "큐브 생성\n", poket )

    testpoket( )

    game = poketCube( )
    game.scramble( )
    state = game.action( 'F' )
    print( state )
