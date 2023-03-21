# Python profilers
Sometimes we want to profile CPU time usage and RAM memory usage. There are multiple tools available.

* cProfile: https://docs.python.org/3/library/profile.html
* Scalene: https://pypi.org/project/scalene/

# YouTube links
* Profiling and optimizing your Python code | Python tricks
  * https://youtu.be/8qEnExGLZfY
  * 심리학자인 유튜버가 친절하게 설명해 준다. 예제는 분명히 최적화되지 않은 코드라는 감이 오지만, 실전에서도 알게 모르게 그런 일들이 충분히 일어날 수 있음을 강조한다.
  * cProfile 모듈을 이용해서 어디에서 계산 시간이 많이 일어나는지를 파악한다. cProfile 도구를 함수에 적용시키는 Decorator(장식자)를 만든다. 이 장식자를 사용해 함수를 돌리는데, 어느 지점에서 계산 시간이 많이 나오는지를 볼 수 있다.
  * 마지막에는 계산 complexity를 exponential 에서 O(n log n)으로 바꿔주며 최적화를 완료한다.
  * 프로파일링하며 살펴보면서 20배 속도 향상을 올렸는데, 궁극적으로는 알고리즘을 바꿔서 1000배 속도 향상을 이루었다 (5000천 개의 entry를 사용했을 때).
* Scalene: a high-performance, high-precision CPU+GPU+memory profiler for Python (PyCon US 2021)
  * https://youtu.be/5iEf-_7mM1k
  * 프로파일러에 대한 전반적인 좋은 설명 포함.
