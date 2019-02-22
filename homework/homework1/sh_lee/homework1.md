인터프리터와 컴파일러
=

인터프리터: (해석 프로그램)
-
>프로그래밍 언어의 소스 코드를 바로 실행하는 컴퓨터 프로그램
또는 환경을 말한다.
이 방식을 쓰는 대표적인 프로그래밍 언어는 **Python**이다.

1. 줄 단위로 번역, 실행되기 때문에 시분할 시스템에 유용하며
2. 원시 프로그램의 변화에 대한 반응이 빠르다.
3. 한 단계씩 테스트와 수정을 하면서 진행시켜 나가는
대화형 언어에 적합하다.

4. 프로그램이 직접 실행되므로 목적 프로그램이 생성되지 않는다.

인터프리터는 실행 시마다 소스 코드를 한 줄씩 기계어로 번역하는 방식이기 때문에
실행 속도는 (정적) 컴파일 언어보다 느리다.
######이를 해결하기 위하여 바이트코드 컴파일러를 이용해 소스 코드를 가상머신 타겟의 바이트코드로 변환하거나, 반복적으로 쓰이는 함수와 클래스 등의 기계어 코드를 캐싱하는 JIT 컴파일러를 인터프리터에 내장하는 방식이 도입되었다.

인터프리터 언어는 프로그램 수정이 간단하다는 장점이 있다.
코드를 한줄씩 실행시킬 수도 있기에
어떤 코드를 작성하고 바로 실행해보고 문제가 있으면
바로바로 수정하는 방식이 가능하다.
이 장점 때문에 인터프리터 언어는 수정이 빈번히 발생하는 용도의
프로그래밍에서 많이 사용된다.
######이 장점을 최대한 살려서 인터프리터를 적극적으로 채용한 것이 스크립트 언어다.

또한 프로그래밍 언어 차원에서 동적인 기능을 지원하기 유리하다.
실행 시간에만 어떤 모듈을 사용할지 결정하는 것이나
사용자가 입력한 임의의 프로그램을 평가하는 것이라던가
심지어 이미 실행되고 있는 코드 자체를 수정하며 실행하는 등의
기능을 구현할 수가 있다.

######디버그를 하는 방식이 구문 오류의 경우 예전 인터프리터의 경우에는 정말로 한줄씩 읽어서 실행했기에 구문 오류가 나오는 부분 전까지는 멀쩡하게 실행되는 경우가 많았다. 그러다보니 실행되지 않는 부분에는 오류가 있어도 오류로 처리되지 않는 경우도 존재하였다. 하지만 최근에는 성능 등의 이유로 파일을 실행하면 파일 전체를 컴파일 하는 방식을 사용하기 때문에 처음부터 구문 오류를 전부 잡아주는 인터프리터도 많아지고 있다.

소스 코드가 쉽게 공개된다는 단점이 있다.
######인터프리터를 주로 사용하는 언어의 경우 바이트코드 등으로 컴파일해서 배포하는 경우도 잘 없을 뿐더러, 지원한다고 해도 컴파일 전/후 언어가 비교적 단순한 편이라서 쉽게 디컴파일이 가능하다.

[인터프리터](https://ko.wikipedia.org/wiki/%EC%9D%B8%ED%84%B0%ED%94%84%EB%A6%AC%ED%84%B0)

컴파일러
-
고급언어로 쓰여진 프로그램(원시 코드)이 컴퓨터에서 수행되기 위해서는
컴퓨터가 직접 이해할 수 있는 언어(기계어)로 바꾸어 주어야 한다.
이러한 일을 하는 프로그램을 컴파일러라고 한다.

* 번역과 실행 과정을 거쳐야 하기 때문에
번역 과정이 번거롭고 번역 시간이 오래 걸리지만,
한번 번역한 후에는 다시 번역하지 않으므로 실행 속도가 빠르다.

* 컴파일러는 소스 코드를 번역해서 실행 파일을 만들기 때문에
프로그램에 수정 사항이 발생하면 소스 코드를 다시 컴파일해야 한다.