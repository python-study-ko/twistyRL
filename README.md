# twistyRL
[**트위스티 퍼즐**이란?](https://ko.wikipedia.org/wiki/%EC%A1%B0%ED%95%A9_%ED%8D%BC%EC%A6%90#.EC.A0.95.EC.9C.A1.EB.A9.B4.EC.B2.B4_.EB.AA.A8.EC.96.91.EC.9D.98_.ED.8A.B8.EC.9C.84.EC.8A.A4.ED.8B.B0_.ED.8D.BC.EC.A6.90)

이 프로젝트는 강화학습(Reinforcement Learning)을 공부하기 위한 트위스티 게임 환경입니다.

흔히 큐브라고도 붙리는 이 게임은 수많은 경우의 수로 인해 해법 공식을 이용해 문제를 풀지 않는 이상 풀기 힘들다고 알려져 있습니다.

이 프로젝트는 그런 트위스트 퍼즐의 해법을 강화학습을 이용해 찾아낼 수 있는지 실험합니다.


## 게임환경

트위스티 게임 환경은 [OpenAI Gym](https://gym.openai.com/)과 유사한 구조를 가집니다.

[//]: # "method 다듬은 뒤 example code 추가"

<!---
Usage
```python
from cuvenv import poketCube
    
cube = poketCube()
state = cube.reset()
next_state, reward, terminal = cube.action("U")
...
```
-->

### 퍼즐 상태의 정의
큐브의 여섯가지 색상은 1~6까지의 숫자로 표현되며, 큐브를 돌리는 행동은 미리 지정된 명령으로 표현됩니다.

U 명령을 수행했을 때 색의 변화 없이 90도 회전하게 되는 면을 윗면으로 두고, 모든 명령은 큐브를 이 방향으로 고정시킨 상태에서 수행됩니다. 

[//]: # "state반환 시 어떤 구조로 반환되는지에 대한 설명 추가 필요"

### 지원되는 퍼즐 사이즈

- [x] 포켓 큐브(2\*2\*2) (TESTING)
- [x] 루빅스 큐브(3\*3\*3) (WIP)
- [ ] 리벤지 큐브(4\*4\*4)
- [ ] 프로페서스 큐브(5\*5\*5)

### 사용 가능한 명령어
아래에 기술되는 명령은 회전 대상이 되는 면을 바라보고 시계방향으로 90˚ 회전한 명령, 반시계방향으로 90˚ 회전한 K'(prime) 명령과 시계반향으로 180˚ 회전한 K2 명령입니다.
실질적으로 공식 큐브 협회에서 규정한 명령어는 모두 사용가능합니다.

**주의**: twistyRL 에서 prime 명령어의 기호는 작은따옴표(')가 아닌 back quote(\`)을 사용하고 있습니다.

1. 포켓큐브:
 - 시계반향 90˚ 회전: U, D, R, L, F, B
 - 반시계반향 90˚ 회전: U\`, D\`, R\`, L\`, F\`, B\`
 - 시계반향 180˚ 회전: U2, D2, R2, L2, F2, B2
 ![](img/포켓큐브.png)
 
2. 루빅스큐브:
 - 시계반향 90˚ 회전: U, D, R, L, F, B
 - 반시계반향 90˚ 회전: U\`, D\`, R\`, L\`, F\`, B\`
 - 시계반향 180˚ 회전: U2, D2, R2, L2, F2, B2
 ![](img/루빅스큐브.png)
 
### 큐브 스크램블
WCA(World Cube Association)에서는 스크램블 프로그램을 이용하도록 [규정](https://www.worldcubeassociation.org/regulations/translations/korean/#5b5)하고 있습니다.

그래서 이 게임 역시 해당 로직을 이용하여 큐브를 섞습니다.

[스크램블 프로그램](https://ruwix.com/puzzle-scramble-generators/rubiks-cube-scrambler/)
: 파이썬으로 작성된 코드는 [여기](https://github.com/Morphage/scrambler)를 참고!


## 논의할 것들
- 보상 문제: reward 책정에 관한 논의가 필요합니다.

