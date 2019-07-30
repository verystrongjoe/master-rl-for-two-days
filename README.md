# master-rl-for-two-days
lecture slides and source codes reinforcement learning for 2 days 

## installation
  - 파이선 Python 3.7.4  설치
    https://www.python.org/downloads/release/python-374/
  - Git 설치 (64-bit Git for Windows Setup)
    https://git-scm.com/downloads
  - 실습 레포지토리 클론
    https://github.com/verystrongjoe/master-rl-for-two-days
    https://github.com/verystrongjoe/master-rl-for-two-days.git

    pip install virtualenv
    C:\>workspace\python>virtualenv ProjectEnv( here venv)
    C:\>workspace\python>cd ProjectEnv\Scripts
    C:\>workspace\python\ProjectEnv\Scripts>activate

  - pip install -r requirement.txt 실행
    https://www.tensorflow.org/install
  - 테스트 돌려보는 스크립트를 만들어볼수 있을려나...
  - check tf.20.py를 실행한다
  - tensorboard를 확인한다. (http://localhost:6006/)
  - mnist & dqn 소스를 돌려본다
  - bandit.py도 돌려본다  
  - cartpole-dqn.py도 돌려본다.

## 실습환경 체크 (19.07.30) 
  - Python 3.7.3 실제 교육장소에 설치된것으로 이걸 테스트하겠음
  - 실습환경 
    . CPU i7-7700 3.60GHZ, 16GB, 64Bit Windows 10 Pro
    . 그래픽 카드 GPU GT 730 2Gb 
     . 384core, 2gb https://www.geforce.com/hardware/desktop-gpus/geforce-gt-730/specifications
     . https://www.reddit.com/r/deeplearning/comments/70wxtd/is_a_geforce_gt_730_suitable_for_a_beginner/
     . https://hiseon.me/data-analytics/tensorflow/tensorflow-requirements/
      . 텐스플로우의 GPU 가속의 기능을 이용하기 위해서 최소 하드웨어 사양으로는 GeForece 750 Ti를 추천해 드립니다.
     . 그냥 CPU로!! 

## Reference
  - Richard Sutton second complete version
    http://incompleteideas.net/book/the-book-2nd.html
  -   
  
## Git issue
아래와 같은 커맨드 날리면 git id/password를 두번 물어보는 일 제거 가능

"""
$ git config --system --unset credential.helper
"""
