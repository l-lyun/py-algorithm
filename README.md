# 알고리즘 공부 연습장

Since 24.12.27

## 디렉토리 구조

```bash
Baekjoon/
  Bronze/
    1000.js
  Silver/
    1000.py
이코테/
  CH1/
    01테스트_문제.py
Study/
  BFS/
    README.md
```

- Baekjoon
  - 백준사이트의 문제를 해결합니다.
  - 파일명은 `<문제번호>.<확장자>`로 합니다.
- 이테코
  - `CH<number>/`: 챕터 번호를 하위 폴더로 합니다.
  - `<number><문제이름>`: 문제 번호와 이름을 띄어쓰기 없이 적습니다.
- Study
  - 알고리즘 개념을 정리합니다.
  - 알고리즘 이름을 폴더로 하여 마크다운을 이용하여 내용을 정리합니다.

## 파일 템플릿

### 주석

각 언어별 블록 주석을 이용합니다.

**필수 항목**

- 문제 링크
- 카테고리
- 문제 해설: 간략하게 문제 해설을 작성합니다.

**선택 항목**

- 참조 링크
- 그 외 부가적 설명

### main 함수

`main`함수를 선언하고, 문제해결에 필요한 로직을 작성합니다.

### 예시

1. `python`

```python
'''
문제 링크: https://www.acmicpc.net/problem/1000
카테고리: 수학
문제 해설: A + B를 계산합니다.

(옵션)참조링크:
'''
def main(a, b):
  return a + b
```

2. `javascript`

```javascript
/**
 * 문제 링크: https://www.acmicpc.net/problem/1000
 * 카테고리: 수학
 * 문제 해설: A + B를 계산합니다.
 *
 * (옵션)참조링크:
 */
const main = (a, b) => {
  return a + b;
};
```

```markdown
### 개요

- close #2
- 문제링크: https://www.acmicpc.net/problem/1000
- 기초 수학문제입니다.

### 카테고리

- 수학

### 문제 해설

A + B 를 계산합니다.
```

### Merge

`squash merge`하기 때문에 branch, commit 컨벤션을 따로 정하지 않습니다.
