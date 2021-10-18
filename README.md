# TEDxPOSTECH Homepage Renewal

## Developer
* lbs1163

## Development Environment
### Basic
* web server: nginx
* middleware: uwsgi
* web framework: django
* database: sqlite

### pip list
* django==2.0.7
* Pillow==5.2.0

## Deploy Process
* 우선 깃에서 변경사항을 다운로드 받아옴  
`git pull`  
* 모든 커멘드는 virtual environment 안에서 동작해야함.  
`workon tedxpostech`  
* 다음, static파일을 모두 root 디렉토리의 static으로 옮겨야 함(장고 기본 스테틱 파일도 옮겨야 함)
`./manage.py collectstatic`  
* 서버를 실행하기 위해 아래 명령어 실행
`./manage.py runserver`
* 혹여나 다른 pip 설치가 필요하다면 반드시 **requirements.txt**에 패키지명과 버전을 넣고 다음 커멘드를 실행하여 설치  
`pip install -r requirements.txt`
