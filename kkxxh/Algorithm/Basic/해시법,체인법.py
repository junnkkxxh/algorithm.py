"""
해시법
'데이터를 저장할 위치= 인덱스'

체인법
해시 충돌의 대처 방법으로
해시값이 같은 원소를 연결리스트로 관리

"""

#체인법으로 해시 함수 구현
from __future__ import annotations
from typing import Any,Type
import hashlib

class Node:
    """해시를 구성하는 노드"""

    def __init__(self, key: Any, value:Any, next:Node) -> None:
        """초기화"""
        self.key = key
        self.value = value
        self.next = next #뒤쪽 노드 참고


class ChainedHash:
    """체인법으로 해시클래스 구현"""
    
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [None] * self.capacity
    
    def hash_value(self, key:Any) -> int:
        """해시값을 구함"""
        if isinstance(key,int):
            return key% self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(),16) %self.capacity)
