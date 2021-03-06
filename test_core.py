from twistyRL import *

if __name__ == "__main__" :
    ## 테스트 코드

    # face 객체 테스트
    sample1 = [ [ 1, 6, 4 ], [ 2, 4, 1 ], [ 4, 5, 1 ] ]
    sample1np = np.array( sample1, dtype=np.uint8 )
    sample2 = [ [ 1, 1, 1 ], [ 1, 1, 1 ], [ 1, 1, 1 ] ]

    # 면의 길이
    n = 3

    # n*n의 면 생성
    newface = face( n )

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
    print( "\n면 상태:\n{matrix}\n완셩여부: {done} 면 점수: {point}".format( matrix=newface.matrix, done=newface.done,
                                                                   point=newface.point ) )
    # get 메소드 테스트
    newface.set( sample1np )
    index1 = "r0"
    index2 = "c1"
    index3 = "r2"

    print( "\n면 상태:\n{matrix}\n완셩여부: {done} 면 점수: {point}".format( matrix=newface.matrix, done=newface.done,
                                                                   point=newface.point ) )

    print( "{index} : {result}".format( index=index1, result=newface.get( index1 ) ) )
    print( "{index} : {result}".format( index=index2, result=newface.get( index2 ) ) )
    print( "{index} : {result}".format( index=index3, result=newface.get( index3 ) ) )

    # change 메소드 테스트
    """
    c1의 값을 r0의 값으로 변경함

    변경전 면상태
    [[1 6 4]
     [2 4 1]
     [4 5 1]]

    r0 == [[1 2 4]]

    변경후 면상태
    [[1 6 4]
     [1 2 4]
     [4 5 1]]
    """
    print( "변경전 면상태\n{matrix}".format( matrix=newface.matrix ) )
    r0 = newface.get( "r0" )
    newface.change( 'c1', r0 )
    print( "변경후 면상태\n{matrix}".format( matrix=newface.matrix ) )

    # reset 메소드 테스트
    newface.reset( 3 )
    print( "면 초기화\n{matrix}".format( matrix=newface.matrix ) )
