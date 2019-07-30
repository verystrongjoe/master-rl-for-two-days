안녕하세요 선혜영프로님

금일 오전 배려해주신 덕분에 델타존B106호 강의장 실습 환경 체크를 잘 마쳤습니다.

기존의 HDD에 추가로 설정하는 부분으로 진행했고, 기존의 파이선 교육이 Python 3.7.3(64bit) 으로 되어있어 저도 버젼 맞추도록 하겠습니다.
GPU가 엔비디아 GTC 730 2GB 모델이어서 4GB면 고려해보겠으나 레딧이나 텐서플로우 공식 사이트에서 언급된 최소사양(GeForece 750 Ti)에도 
못미쳐서 CPU로 진행하도록 하겠습니다. CPU i7-7700 3.60GHZ, 16GB, 64Bit Windows 10 Pro 스펙이면 우선 기초과정 진행에는 어려움이 없습니다.
향후 심화과정에서는 GPU가 필요할지도 모르니 참고바라구요, 얘기된데로 8/14일날 제가 앉은 자리의 HDD를 다 통일해서 강의장 PC 전체에 셋팅해주시면 될 것 같습니다.
그렇지만, 점검차원에서 설치 가이드는 다 배포후 빠르게 훑을 거구요, 

제가 금일 제 PC HDD에서 작업한 내용들입니다. 
1. 파이선 Python 3.7.3 설치 https://www.python.org/downloads/release/python-373/
2. Git 설치 (64-bit Git for Windows Setup) https://git-scm.com/downloads
3. Git 소스복제 https://github.com/verystrongjoe/master-rl-for-two-days https://github.com/verystrongjoe/master-rl-for-two-days.git
4. 가상환경 설정 (pip install virtualenv)
C:>workspace\python>virtualenv ProjectEnv( here venv) C:>workspace\python>cd ProjectEnv\Scripts C:>workspace\python\ProjectEnv\Scripts>activate
5. 관련 모든 라이브러리 설치
pip install -r requirement.txt 실행 https://www.tensorflow.org/install
6. Pycharm community version 설치 (any recent version is ok) 
https://www.jetbrains.com/pycharm/download/

우선 실습시 필요한 텐서플로우 2.0과 그리고 텐서보드 그리고 간단한 강화학습 코드는 이미 구현해서 돌려보고 정상 동작 확인했으니
최종점검은 말씀드린데로 스킵하겠습니다. (시간이 없어요 ㅜ)

아래는 위의 내용 레퍼런스입니다.
Specification https://www.geforce.com/hardware/desktop-gpus/geforce-gt-730/specifications 
Reddit https://www.reddit.com/r/deeplearning/comments/70wxtd/is_a_geforce_gt_730_suitable_for_a_beginner/ 
Tensorflow GPU Minimum required specifications https://hiseon.me/data-analytics/tensorflow/tensorflow-requirements/ 


그럼 좋은하루되세요,
