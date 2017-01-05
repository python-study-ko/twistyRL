# twistyRL
트위스티 퍼즐을 수행하는 가상 게임 환경을 만들고 이를 바탕으로 다양한 강화학습을 학습하는 프로젝트입니다.
누구나 참여 하실 수 있으며 스스로 제작한 가상환경을 바탕으로 좀더 빠른 학습을 하기 위함입니다.

# [트위스티 퍼즐](https://ko.wikipedia.org/wiki/%EC%A1%B0%ED%95%A9_%ED%8D%BC%EC%A6%90#.EC.A0.95.EC.9C.A1.EB.A9.B4.EC.B2.B4_.EB.AA.A8.EC.96.91.EC.9D.98_.ED.8A.B8.EC.9C.84.EC.8A.A4.ED.8B.B0_.ED.8D.BC.EC.A6.90)
흔히 큐브라고도 붙리는 이 게임은 다양하게 많은 변수로 인해 특정 공식을 이용해여 문제를 풀지 않느 이상 풀기 힘들다고 알려져 있습니다.
이 프로젝트는 그런 트위스트 퍼즐을 강화학습을 통하여 스스로 그러한 공식을 찾아 내고 이를 통해 실제로 문제를 해결 할수 있는지를 실험 하기 위함 입니다.
일단 큐브는 가장 쉬운 포켓큐브(2*2*2)부터 시작하여 가장 유명한 루빅스 큐브(3*3*3)와 그외 리벤지,프로페서스 큐브등의 순으 구축해보려 합니다.

# 게임환경
트위스티 게임 환경은 openAI의 Gym과 유사한 구조를 가집니다.
먼저 큐브의 여섯가지 색상은 1~6까지의 숫자로 표현되며, 상하,좌우로 큐브를 돌릴 수 있는 경우의 수는 행동으로 표현됩니다.
그리고 육면체의 각 면은 숫자로 표현되며 주사위 처럼 숫자를 부여할 것입니다. 이때 가장 위에서 보이는 면의 번호는 무조건 1이라고 하겠습니다.
즉, 가장 위에서 보이는 면(1번 면)을 기준으로 행동을 취할 것이며 이때 나온 결과를 상태로 플레이어에게 알려줄 것입니다.

## 이슈
- 보상 문제: 강화 학습시 어떻게 보상을 줘야 하는지에 대한 의논이 필요합니다. 게임 특성상 게임이 끝나기 전까지는 보상이 없기때문에
다양한 실험을 통해 최적의 보상 방법을 찾아야한다.

## 구현된 가상환경

## 구현 예정인 가상환경

- 포켓 큐브(2*2*2)
- 루빅스 큐브(3*3*3)
- 리벤지 큐브(4*4*4)
- 프로페서스 큐브(5*5*5)