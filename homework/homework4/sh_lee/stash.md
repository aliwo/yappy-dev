stashing
========
unstaged 상태인 변경사항을 일시적으로 백업하고 워킹디렉토리를 깨끗한 상태로 유지합니다.
> 커밋하지 않고 잠시 브랜치를 변경하고 다시 돌아와서 작업을 다시 하고 싶은 경우 사용

> 워킹 디렉토리에서 수정한 파일만(Modified이면서 Tracked 상태인 파일과 Staging area에 있는 파일들을) 스택에 저장

<pre><code>git stash</code></pre>
현재의 변경사항이 저장되고 워킹디렉토리는 HEAD 상태로 돌아가게 됩니다.

이제 워킹디렉토리가 깨끗해졌으므로 rebase나 pull 같은 작업을 정상적으로 할 수 있습니다.

상태
* working directory: 작업 디렉토리
* Index: Staging area(준비 영역)
* HEAD: 최종 확정본

working directory -> add -> Index -> commit -> HEAD

* Untracked: 관리 대상이 아님
* Tracked: 관리 대상임
* Unmodified: 수정하지 않음
* Modified: 수정함
* Staged: 커밋하면 저장소에 기록되는 상태

<pre><code>git stash list # 저장한 내역 조회
git stash show stash이름 # stash의 자세한 내용
git stash pop # stash에 저장한 내용을 워킹디렉토리에 적용하고 stash 내역에서 제거
git stash apply # 제거하지 않고 적용
git stash apply --index # Staged 상태까지 복원
git stash drop # Stash 제거
git stash show -p | git apply -R # 가장 최근의 Stash를 사용하여 다시 되돌려 놓는다.
git stash branch # Stash할 당시의 커밋을 Checkout한 후 새로운 브랜치를 만들고 여기에 적용한 후, Stash를 삭제한다.</code></pre>
