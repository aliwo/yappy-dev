컴파일러와 인터프리터 둘 다 C나 JAVA같은 고레벨언어로 작성된 프로그래밍 언어를 컴퓨터가 이해할 수 있는 기계어로 변환한다. 
그러나 그 과정에 있어서 컴파일러와 인터프리터는 차이를 보인다.

컴파일러는 전체소스코드를 보고 명령어를 수집하고 재구성하는 반면 
인터프리터는 소스코드의 각 행을 연속적으로 분석하며 실행한다.
즉, 컴파일러는 소스코드 전체를 한 번 훑고 컴퓨터 프로세서가 실행할 수 있도록 바로 기계어로 변환하는 반면
인터프리터는 각 행마다 고레벨 언어를 중간 코드로 변환한다. 

컴파일러는 전체 소스 코드를 기계어로 미리 번역해두기 때문에 실행 속도가 빠르고 메모리를 적게 차지한다.
그러나 한 번에 번역하는 특성 상 처음에는 메모리가 생성되고 번역하는 데에 시간이 오래 걸린다.
반면에 인터프리터는 실행 파일을 만들지 않고 직접 실행하기 때문에 간편하다. 
직접 실행하므로 오류가 발생하면 그때마다 빠르게 알려줄 수 있고 디버깅도 쉽다.

컴파일러는 전체 소스코드를 변환한 뒤 에러를 보고하지만 인터프리터는 각 행마다 실행하는 도중에 에러가 보고되면 이후 작성된 코드를 살펴보지 않는다.
이는 보안적인 관점에서 도움이 된다.

인터프리터 언어에는 python이 있고 컴파일러 언어에는 C, C++ 등이 있다.
JAVA는 인터프리터, 컴파일러 모두를 사용한다.