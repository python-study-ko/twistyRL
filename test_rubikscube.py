from cuvenv import *


def testrubiks( ) :
    """
    포켓큐브 회전 개발용 테스트 함수
    :return:
    """

    sampleCube = {
        1 : [ [ 11, 12, 13 ], [ 14, 15, 16 ], [ 17, 18, 19 ] ], 2 : [ [ 21, 22, 23 ], [ 24, 25, 26 ], [ 27, 28, 29 ] ],
        3 : [ [ 31, 32, 33 ], [ 34, 35, 36 ], [ 37, 38, 39 ] ],
        4 : [ [ 41, 42, 43 ], [ 44, 45, 46 ], [ 47, 48, 49 ] ], 5 : [ [ 51, 52, 53 ], [ 54, 55, 56 ], [ 57, 58, 59 ] ],
        6 : [ [ 61, 62, 63 ], [ 64, 65, 66 ], [ 67, 68, 69 ] ]
    }

    def reset( cube, mat=sampleCube ) :
        for i in range( 1, 7 ) :
            cube.cube[ i ].set( mat[ i ] )
            cube.history = [ ]
        return cube

    # 회전 테스트
    rubiks = rubiksCube( )
    turnset = ('F', 'F`', 'R', 'R`', 'U', 'U`', 'B', 'B`', 'L', 'L`', 'D', 'D`')
    # 180도 회전 명령어
    double = [x+'2' for x in turnset if x[-1] != '`']

    print( "회전 테스트" )
    for act in turnset :
        rubiks = reset( rubiks )
        rubiks.action( act )
        print( "{act} 실행:\n{cube}".format( act=act, cube=rubiks ) )

    print( "180도 회전 테스트" )
    for act in double :
        rubiks = reset( rubiks )
        rubiks.action( act )
        print( "{act} 실행:\n{cube}".format( act=act, cube=rubiks ) )

    # 실제로 퍼즐이 맞춰지는지 테스트
    print( "============\n실제 테스트\n섞어 놓은 큐브와 해답을 이용하여 제대로 맞춰지는지 검증" )
    Q = {
        1 : [ [ 4, 6, 2 ], [ 4, 3, 2 ], [ 5, 5, 2 ] ], 2 : [ [ 3, 5, 4], [ 6, 5, 1 ], [ 5, 3, 4 ] ],
        3 : [ [ 1, 2, 6 ], [ 1, 1, 6 ], [ 2, 1, 3 ] ],
        4 : [ [ 1, 3, 6 ], [ 3, 6, 2 ], [ 1, 4, 4 ] ], 5 : [ [ 6, 4, 3 ], [ 4, 2, 2 ], [ 3, 5, 1 ] ],
        6 : [ [ 2, 3, 5 ], [ 1, 4, 5 ], [ 5, 6, 6 ] ]
    }
    solve = [ 'L', 'D', 'L`', 'L`', 'U`', 'D', 'B', 'R`', 'D`', 'U`', 'L`', 'L`' ]

    rubiks = rubiksCube( )
    rubiks = reset( rubiks, Q )

    for act in solve :
        done,point,count,_=rubiks.action( act )
        print("{}. 회전방향: {} | 완료여부: {} | 점수: {}".format(count,act,done,point))
    print( rubiks )

if __name__ == "__main__" :
    ## 테스트 코드
    # 포켓큐브 생성
    rubiks = rubiksCube( )
    print( "큐브 생성\n", rubiks )

    testrubiks( )
