트리,재귀
-
- 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
- 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
- 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)

1. 트리 정보 dict로 정리
2. 함수의 종료조건 자식 노드가 더 이상 없는 경우 return
3. 재귀적으로 함수를 호출하면서 전위, 중위, 후위 순회의 규칙을 고려해 root 노드 print
