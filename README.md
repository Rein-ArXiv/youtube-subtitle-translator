# YouTube Subtitle Translator

YouTube 동영상의 자막을 간단하게 추출하고 번역하여 SRT 파일로 다운로드할 수 있는 웹 애플리케이션입니다.

## 주요 기능

- 🎬 **YouTube URL 입력**만으로 자막 추출
- 🌍 **17개 언어** 번역 지원
- ⚡ **실시간 번역 미리보기**
- 📥 **SRT 파일 다운로드**
- 🎯 **YouTube 내장 번역 엔진** 사용으로 고품질 번역

## 지원 언어

한국어, 영어, 일본어, 중국어(간체/번체), 스페인어, 프랑스어, 독일어, 이탈리아어, 포르투갈어, 러시아어, 아랍어, 힌디어, 태국어, 베트남어, 인도네시아어, 터키어

## 설치 방법

```bash
# 레포지토리 클론
git clone <repository-url>
cd <repository-name>

# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt
```

## 사용 방법

```bash
# 애플리케이션 실행
python app.py

# 웹 브라우저에서 접속
# http://localhost:5000
```

1. YouTube URL 입력
2. 번역할 언어 선택
3. "자막 추출 및 번역 시작" 버튼 클릭
4. 실시간 미리보기 확인
5. 완료 후 SRT 파일 다운로드

## 기술 스택

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS (Tailwind), JavaScript (jQuery)
- **YouTube API**: youtube-transcript-api
- **Translation**: YouTube 내장 번역 시스템

## 프로젝트 구조

```
├── app.py                 # Flask 애플리케이션 메인
├── module/
│   └── youtube_module.py  # YouTube 자막 추출 모듈
├── templates/
│   └── index.html        # 웹 인터페이스
├── requirements.txt      # Python 의존성
└── README.md            # 프로젝트 문서
```

## 라이센스

MIT License

## 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
